# dashboard/routes.py

from flask import Blueprint, render_template, request, redirect, flash, session
from database import insert_into_table

dashboard_bp = Blueprint('dashboard', __name__, template_folder='../templates')

# Dashboard home
@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html', user=session['user'])

# Add Student
@dashboard_bp.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "subject": request.form['subject'],
            "score": int(request.form['score'])
        }
        try:
            insert_into_table('Student', data)
            flash("Student added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error adding student: {e}", "danger")
    return render_template('add_student.html')

# Add Batch
@dashboard_bp.route('/add-batch', methods=['GET', 'POST'])
def add_batch():
    if request.method == 'POST':
        data = {
            "batch_name": request.form['batch_name'],
            "year": int(request.form['year'])
        }
        try:
            insert_into_table('Batch', data)
            flash("Batch added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error adding batch: {e}", "danger")
    return render_template('add_batch.html')

# Add Answer Schema
@dashboard_bp.route('/add-answer-schema', methods=['GET', 'POST'])
def add_answer_schema():
    if request.method == 'POST':
        data = {
            "subject": request.form['subject'],
            "file_name": request.form['file_name'],
            "file_link": request.form['file_link']
        }
        try:
            insert_into_table('answer_schema', data)
            flash("Answer schema added successfully!", "success")
            return redirect('/dashboard')
        except Exception as e:
            flash(f"Error adding answer schema: {e}", "danger")
    return render_template('add_answer_schema.html')
