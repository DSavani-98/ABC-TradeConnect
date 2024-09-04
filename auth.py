from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User

def init_auth_routes(app):

    @app.route('/login', methods=['POST'])
    def login():
        emailId = request.json.get('emailId', None)
        password = request.json.get('password', None)
        user = User.query.filter_by(emailId=emailId).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=emailId)
            return jsonify(access_token=access_token)
        return jsonify({"msg": "Bad emailId or password"}), 401

    @app.route('/logout', methods=['POST'])
    @jwt_required()
    def logout():
        # JWTs are automatically blacklisted on expiration
        return jsonify({"msg": "Successfully logged out"}), 200