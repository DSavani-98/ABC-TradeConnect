from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emailId = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(120), unique=True, nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date)
    password = db.Column(db.String(300), nullable=False)
    createdOn = db.Column(db.Date)
    isEnabled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Users {self.lastName} {self.firstName}>"