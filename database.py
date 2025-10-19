# database.py

from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Supabase credentials
SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

# ---------------------- Student Table ----------------------

def get_all_students():
    """Fetch all student records."""
    response = supabase.table('Student').select('*').execute()
    return response.data

def insert_student(student_data):
    """Insert a new student record."""
    response = supabase.table('Student').insert(student_data).execute()
    return response.data

def update_student(student_id, updated_data):
    """Update student record by ID."""
    response = supabase.table('Student').update(updated_data).eq('id', student_id).execute()
    return response.data

def delete_student(student_id):
    """Delete student record by ID."""
    response = supabase.table('Student').delete().eq('id', student_id).execute()
    return response.data

# ---------------------- Batch Table ----------------------

def get_all_batches():
    """Fetch all batch records."""
    response = supabase.table('Batch').select('*').execute()
    return response.data

def insert_batch(batch_data):
    """Insert a new batch record."""
    response = supabase.table('Batch').insert(batch_data).execute()
    return response.data

def update_batch(batch_id, updated_data):
    """Update batch record by ID."""
    response = supabase.table('Batch').update(updated_data).eq('id', batch_id).execute()
    return response.data

def delete_batch(batch_id):
    """Delete batch record by ID."""
    response = supabase.table('Batch').delete().eq('id', batch_id).execute()
    return response.data

# ---------------------- Answer Schema Table ----------------------

def get_all_answer_schemas():
    """Fetch all answer schema records."""
    response = supabase.table('answer_schema').select('*').execute()
    return response.data

def insert_answer_schema(schema_data):
    """Insert a new answer schema record."""
    response = supabase.table('answer_schema').insert(schema_data).execute()
    return response.data

def update_answer_schema(schema_id, updated_data):
    """Update answer schema record by ID."""
    response = supabase.table('answer_schema').update(updated_data).eq('id', schema_id).execute()
    return response.data

def delete_answer_schema(schema_id):
    """Delete answer schema record by ID."""
    response = supabase.table('answer_schema').delete().eq('id', schema_id).execute()
    return response.data