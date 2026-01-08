from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector

admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='balaguer_db'
    )

# Admin dashboard (READ)
@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    if session.get('role') != 'admin':
        return redirect(url_for('auth_bp.login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_tb")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('admin_dashboard.html', users=users, username=session.get('username'))

# ADD (CREATE)
@admin_bp.route('/admin/add', methods=['POST'])
def add_user():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    birthdate = request.form['birthdate']
    address = request.form['address']
    mobile_number = request.form['mobile_number']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['user_type']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user_tb (firstname, lastname, birthdate, address, mobile_number, email, username, password, user_type)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (firstname, lastname, birthdate, address, mobile_number, email, username, password, user_type))
    conn.commit()
    cursor.close()
    conn.close()

    flash("User added successfully!")
    return redirect(url_for('admin_bp.admin_dashboard'))

# UPDATE
@admin_bp.route('/admin/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    birthdate = request.form['birthdate']
    address = request.form['address']
    mobile_number = request.form['mobile_number']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    user_type = request.form['user_type']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_tb
        SET firstname=%s, lastname=%s, birthdate=%s, address=%s, mobile_number=%s, email=%s, username=%s, password=%s, user_type=%s
        WHERE user_id=%s
    """, (firstname, lastname, birthdate, address, mobile_number, email, username, password, user_type, user_id))
    conn.commit()
    cursor.close()
    conn.close()

    flash("User updated successfully!")
    return redirect(url_for('admin_bp.admin_dashboard'))

# DELETE
@admin_bp.route('/admin/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_tb WHERE user_id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("User deleted successfully!")
    return redirect(url_for('admin_bp.admin_dashboard'))

# LOGOUT
@admin_bp.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))
