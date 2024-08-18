from flask import Flask, request, render_template, redirect, url_for
from extensions import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
