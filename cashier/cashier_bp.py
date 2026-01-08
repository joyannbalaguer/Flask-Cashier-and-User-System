from flask import Blueprint, render_template, session, redirect, url_for

cashier_bp = Blueprint('cashier_bp', __name__, template_folder='templates')

@cashier_bp.route('/cashier/dashboard')
def cashier_dashboard():
    if session.get('role') != 'cashier':
        return redirect(url_for('auth_bp.login'))
    return render_template('cashier_dashboard.html', username=session.get('username'))

@cashier_bp.route('/cashier/logout')
def cashier_logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))
