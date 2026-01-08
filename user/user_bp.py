from flask import Blueprint, render_template, session, redirect, url_for

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/user/dashboard')
def user_dashboard():
    if session.get('role') != 'user':
        return redirect(url_for('auth_bp.login'))
    return render_template('user_dashboard.html', username=session.get('username'))

@user_bp.route('/user/logout')
def user_logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))
