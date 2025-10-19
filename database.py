# database.py

from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

def insert_into_table(table_name, data):
    """
    Generic insert function for any Supabase table.
    :param table_name: str - name of the table
    :param data: dict - data to insert
    :return: response from Supabase
    """
    return supabase.table(table_name).insert(data).execute()