from flask import Flask
from models import db, Users

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dhruv_abctech:dABCtech1912@localhost/abc_mart'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)   # Initialize the app for use with this database setup

    @app.route('/init_db')
    def init_db():
        db.create_all()
        return "Database tables created!"

    @app.route('/')
    def home():
        return 'Hello, ABCMart!'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)