from flask import Flask, jsonify
from models import db, Users
from flask_jwt_extended import JWTManager





def create_app():
    app = Flask(__name__)

    # Configuring the database connection
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dhruv_abctech:dABCtech1912@localhost/abc_mart'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure the secret key for JWT
    app.config['JWT_SECRET_KEY'] = 'ABCEventTech@2024'  # Change this to a real, secure secret key

    db.init_app(app)   # Initialize the app for use with this database setup

    # Initialize the JWT manager
    jwt = JWTManager(app)   

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'msg': 'Your token has expired',
            'err': 'token_expired'
        }), 401

    @app.route('/init_db')
    def init_db():
        db.create_all()
        return "Database tables created!"

    @app.route('/')
    def home():
        return 'Welcome to ABCMart!!!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)