# auth/routes.py

from flask import Blueprint, render_template, request, redirect, session, flash
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

auth_bp = Blueprint('auth', __name__, template_folder='../templates')

SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = supabase.auth.sign_up({"email": email, "password": password})
            if getattr(response, "user", None):
                flash("Sign-up successful. Please log in.", "success")
                return redirect('/login')
            flash(str(getattr(response, "error", None)), "danger")
        except Exception as e:
            flash(str(e), "danger")
    return render_template('signup.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            if getattr(response, "session", None):
                session['user'] = response.user.email
                return redirect('/dashboard')
            flash("Login failed: " + str(getattr(response, "error", None)), "danger")
        except Exception as e:
            flash("Login failed: " + str(e), "danger")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect('/')