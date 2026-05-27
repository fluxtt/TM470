from flask import Blueprint, render_template, session, redirect, url_for
from app.database.db import get_db_connection

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/dashboard')

def dashboard():
    # protect the dashboard route
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT *
    FROM items
    ORDER BY item_name ASC
    """
    
    cursor.execute(query)
    
    items = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template(
        'dashboard.html',
        items=items
    )
    