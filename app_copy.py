from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dhruv_abctech:dABCtech1912@localhost/abc_mart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# # Define the database schema for the User table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.username

# Route to create the database tables
@app.route('/init_db')
def init_db():
    db.create_all()
    return "Database tables created!"

@app.route('/')
def init():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)