from flask import Flask, render_template, request, redirect, session, flash
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from dashboard.routes import dashboard_bp

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Secret key for session management
app.secret_key = os.getenv("FLASK_SECRET_KEY") or os.urandom(24)

# Supabase credentials
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Missing Supabase credentials: set NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY in your .env")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = supabase.auth.sign_up({"email": email, "password": password})
            if getattr(response, "user", None):
                flash("Sign-up successful. Please log in.", "success")
                return redirect('/login')
            error = getattr(response, "error", None) or response
            flash(str(error), "danger")
        except Exception as e:
            flash(str(e), "danger")
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if getattr(response, "session", None):
                session['user'] = response.user.email
                return redirect('/dashboard')
            error = getattr(response, "error", None) or response
            flash("Login failed: " + str(error), "danger")
        except Exception as e:
            flash("Login failed: " + str(e), "danger")
    return render_template('dashboard.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    
       
    return render_template('dashboard.html', user=session['user'])

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    from dashboard.routes import dashboard_bp
app.register_blueprint(dashboard_bp)