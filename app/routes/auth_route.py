from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.database.db import get_db_connection
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = 'SELECT * FROM users WHERE username = %s'
        cursor.execute(query, (username,))
        
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            stored_password = user['password_hash']
            
            if bcrypt.checkpw(
                password.encode('utf-8'),
                stored_password.encode('utf-8')
            ):
                session['user_id'] = user['id']
                session['username'] = user['username']
                session['role'] = user['role']
                
                return redirect(url_for('inventory.dashboard'))
            
        flash('Invalid username or password', 'danger')
        
    return render_template('login.html')