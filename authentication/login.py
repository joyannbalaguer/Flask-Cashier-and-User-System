from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector

# Blueprint setup
auth_bp = Blueprint('auth_bp', __name__, template_folder='templates')

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',       # your MySQL username
        password='',       # your MySQL password
        database='balaguer_db'
    )

# Login route
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to MySQL with buffered cursor to prevent "Unread result found"
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)
        cursor.execute(
            "SELECT * FROM user_tb WHERE username=%s AND password=%s",
            (username, password)
        )
        user = cursor.fetchone()  # fetch first row
        cursor.close()
        conn.close()

        if user:
            # Store user info in session
            session['user_id'] = user['user_id']
            session['firstname'] = user['firstname']
            session['lastname'] = user['lastname']
            session['birthdate'] = str(user['birthdate'])
            session['address'] = user['address']
            session['mobile_number'] = user['mobile_number']
            session['email'] = user['email']
            session['role'] = user['user_type']
            session['username'] = user['username']

            # Redirect based on role
            if user['user_type'] == 'user':
                return redirect(url_for('user_bp.user_dashboard'))
            elif user['user_type'] == 'cashier':
                return redirect(url_for('cashier_bp.cashier_dashboard'))
        else:
            flash("Incorrect credentials, please try again.")

    return render_template('login.html')
