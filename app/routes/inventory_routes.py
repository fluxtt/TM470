from flask import Blueprint, render_template, session, redirect, url_for, request, flash
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
    
@inventory_bp.route('/add-transaction', methods=['POST'])
def add_transaction():
    if "user_id" not in session:
        return redirect(url_for('auth.login'))
    
    item_id = request.form["item_id"]
    adjustment = int(request.form["adjustment"])
    note = request.form["note"]
    user_id = session["user_id"]
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # GET CURRENT ITEM
    
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    current_quantity = item["quantity"]
    new_quantity = current_quantity + adjustment
    
    # PREVENT NEGATIVE STOCK
    if new_quantity < 0:
        flash("Cannot reduce stock below zero.", "error")
        return redirect(url_for('inventory.dashboard'))
    
    # UPDATE ITEM QUANTITY
    cursor.execute(
        """
        UPDATE items
        SET quantity = %s
        WHERE id = %s
        """,
        (new_quantity, item_id)
    )
    
    # DETERMINE TRANSACTION TYPE
    transaction_type = "in" if adjustment > 0 else "out"
    
    # INSERT TRANSACTION RECORD
    cursor.execute(
        """
        INSERT INTO transactions (
            item_id,
            user_id,
            transaction_type,
            quantity,
            note
            )
            VALUES (%s, %s, %s, %s, %s)
        """,
        (item_id, user_id, transaction_type, abs(adjustment), note)
    )
    
    conn.commit()
    cursor.close()
    conn.close()
    
    flash("Transaction recorded successfully.", "success")
    return redirect(url_for('inventory.dashboard'))
    
@inventory_bp.route('/transactions')
def transaction_history():
    
    if "user_id" not in session:
        return redirect(url_for('auth.login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT
        transactions.id,
        items.item_name,
        users.username,
        transactions.transaction_type,
        transactions.quantity,
        transactions.note,
        transactions.created_at
        
    FROM transactions
    
    JOIN items
        ON transactions.item_id = items.id
        
    JOIN users
        ON transactions.user_id = users.id
        
    ORDER BY transactions.created_at DESC    
    """

    cursor.execute(query)
    
    transactions = cursor.fetchall()
    
    # Needed for transacton modal dropdown
    cursor.execute("SELECT * FROM items ORDER BY item_name ASC")
    items = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template(
        "transactions.html",
        transactions=transactions,
        items=items
    )