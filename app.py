from flask import Flask
from authentication.login import auth_bp
from user.user_bp import user_bp
from cashier.cashier_bp import cashier_bp
from admin_bp import admin_bp
app = Flask(__name__)
app.secret_key = "secret123"

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(cashier_bp)
app.register_blueprint(admin_bp)
if __name__ == "__main__":
    app.run(debug=True)
