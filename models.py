from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailId = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(300))
    firstName = db.Column(db.String(120), unique=True, nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date)
    createdOn = db.Column(db.Date)
    isEnabled = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Users {self.lastName} {self.firstName}>"