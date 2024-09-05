from flask import render_template, redirect, url_for, flash, request, jsonify
from .formsValidation import RegistrationForm
from werkzeug.security import generate_password_hash
from models import db, Users
from flask_jwt_extended import jwt_required, create_access_token
import datetime

def init_auth_routes(app):

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():  # This checks if it's a POST request and validates the form
            hashed_password = generate_password_hash(form.password.data)
            new_user = Users(
                emailId=form.email.data,
                password_hash=hashed_password,
                firstName=form.firstName.data,
                lastName=form.lastName.data,
                birthdate=form.birthdate.data if form.birthdate.data else None,
                createdOn=datetime.datetime.now(),
                isEnabled=form.isEnabled.data
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Congratulations, registration successful!', 'success')
            return redirect(url_for('some_function'))  # Make sure 'some_function' is defined in your routes
        elif request.method == 'POST':
            return jsonify({'errors': form.errors}), 400
        return render_template('register.html', title='Register', form=form)

    @app.route('/login', methods=['POST'])
    def login():
        emailId = request.json.get('emailId', None)
        password = request.json.get('password', None)
        user = Users.query.filter_by(emailId=emailId).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=emailId)
            return jsonify(access_token=access_token)
        return jsonify({"msg": "Bad email or password"}), 401

    @app.route('/logout', methods=['POST'])
    @jwt_required()
    def logout():
        # JWTs are automatically blacklisted on expiration
        return jsonify({"msg": "Successfully logged out"}), 200






























# from flask import jsonify, request
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from werkzeug.security import generate_password_hash
# from models import db, User


# def init_auth_routes(app):

#     @app.route('/register', methods=['POST'])
#     def register():
#         # Extract data from request
#         username = request.json.get('username', None)
#         password = request.json.get('password', None)
#         email = request.json.get('email', None)

#         # Basic validation
#         if not username or not password or not email:
#             return jsonify({"msg": "Missing username, password, or email"}), 400

#         # Check if user already exists
#         if User.query.filter_by(username=username).first() is not None:
#             return jsonify({"msg": "Username already exists"}), 409

#         # Hash the password
#         hashed_password = generate_password_hash(password)

#         # Create new user instance
#         new_user = User(username=username, password_hash=hashed_password, email=email)

#         # Add new user to database
#         db.session.add(new_user)
#         db.session.commit()

#         return jsonify({"msg": "User registered successfully"}), 201

#     @app.route('/login', methods=['POST'])
#     def login():
#         emailId = request.json.get('emailId', None)
#         password = request.json.get('password', None)
#         user = User.query.filter_by(emailId=emailId).first()
#         if user and user.check_password(password):
#             access_token = create_access_token(identity=emailId)
#             return jsonify(access_token=access_token)
#         return jsonify({"msg": "Bad emailId or password"}), 401

#     @app.route('/logout', methods=['POST'])
#     @jwt_required()
#     def logout():
#         # JWTs are automatically blacklisted on expiration
#         return jsonify({"msg": "Successfully logged out"}), 200