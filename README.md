# Flask Cashier and User System

This project is a Flask-based web application that implements a simple role-based authentication system using MySQL as the backend database.

The system supports two roles:
- Cashier (acts as the administrative role)
- User (standard authenticated user)

The application is designed as an academic project to demonstrate backend authentication, session handling, and role-based access control using Flask Blueprints.

## Features

- User authentication using username and password
- Role-based access control (Cashier and User)
- Session-based login and logout
- Separate dashboards per role
- Modular Flask Blueprint structure
- MySQL database integration

## Technology Stack

- Python (Flask)
- MySQL
- HTML / CSS
- mysql-connector-python

## Project Structure

- authentication/  
  Handles login logic and database connection

- cashier/  
  Cashier routes and dashboard

- user/  
  User routes and dashboard

- templates/  
  HTML templates for dashboards and login

- app.py  
  Application entry point and Blueprint registration
  
  ## System Architecture Overview

- Flask application structured using Blueprint architecture
- Separation of concerns between authentication, cashier, and user modules
- Centralized session handling
- MySQL database connection using `mysql-connector-python`
- Jinja2 templates for dynamic HTML rendering

  ## Technology Stack

- Backend: Flask (Blueprint-based architecture)
- Database: MySQL (XAMPP / phpMyAdmin)
- Authentication: Session-based login
- Frontend: HTML, CSS
- Templates: Jinja2
- Database Connector: mysql-connector-python

## Notes

- Passwords are stored as plain text for simplicity (academic use only)
- No registration page is included; users are inserted directly into the database
- The Cashier role functions as the system administrator

## Author

Joy Ann Balaguer
