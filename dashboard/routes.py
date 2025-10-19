# dashboard/routes.py

from flask import Blueprint, render_template, session
from database import get_all_students

dashboard_bp = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    students = get_all_students()
    return render_template('dashboard.html', user=session['user'], students=students)