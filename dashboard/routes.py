# dashboard/routes.py

from flask import Blueprint, render_template, request, redirect, flash, session
from database import insert_student, insert_batch, insert_answer_schema

dashboard_bp = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'])

@dashboard_bp.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "subject": request.form['subject'],
            "score": int(request.form['score'])
        }
        try:
            insert_student(data)
            flash("Student added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error: {e}", "danger")
    return render_template('add_student.html')

@dashboard_bp.route('/add-batch', methods=['GET', 'POST'])
def add_batch():
    if request.method == 'POST':
        data = {
            "batch_name": request.form['batch_name'],
            "year": int(request.form['year'])
        }
        try:
            insert_batch(data)
            flash("Batch added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error: {e}", "danger")
    return render_template('add_batch.html')

@dashboard_bp.route('/add-answer-schema', methods=['GET', 'POST'])
def add_answer_schema():
    if request.method == 'POST':
        data = {
            "subject": request.form['subject'],
            "file_name": request.form['file_name'],
            "file_link": request.form['file_link']
        }
        try:
            insert_answer_schema(data)
            flash("Answer schema added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error: {e}", "danger")
    return render_template('add_answer_schema.html')# dashboard/routes.py

