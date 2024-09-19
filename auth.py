from flask import request, jsonify, redirect, url_for, flash
from .formsValidation import RegistrationForm
from models import db, Users
from flask_jwt_extended import jwt_required, create_access_token
import datetime

def init_auth_routes(app):

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'GET':
            return 'Registration endpoint. Use POST to submit data.'
        
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = Users.set_password(form.password.data)  # Using the static method correctly
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
            return jsonify({'message': 'User registered successfully'}), 201  # Changed to API-friendly response
        return jsonify({'errors': form.errors}), 400

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
        return jsonify({"msg": "Successfully logged out"}), 200
    
    def testRoutes():
        print("This is a test for checking the routes!!!")