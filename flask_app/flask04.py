# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # create an app
from database import db
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db.init_app(app)
with app.app_context():
    db.create_all() 



class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    note = db.Column(db.String(400), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id


# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user = {'firstname': 'Braxton ', 'lastname': 'Talbert', 'email': 'btalber5@uncc.edu'}
    return render_template('index.html', user=a_user)


@app.route('/notes')
def get_notes():
    a_user = {'firstname': 'Braxton ', 'lastname': 'Talbert', 'email': 'btalber5@uncc.edu'}

    return render_template('notes.html', notes=notes, user=a_user)


@app.route('/notes/<note_id>')
def get_note(note_id):
    a_user = {'firstname': 'Braxton ', 'lastname': 'Talbert', 'email': 'btalber5@uncc.edu'}
    return render_template('note.html', note=notes[int(note_id)], user=a_user)


@app.route('/notes/new', methods=['GET', 'POST'])
def new_note():
    a_user = {'firstname': 'Braxton ', 'lastname': 'Talbert', 'email': 'btalber5@uncc.edu'}
    print("request method is ", request.method)

    if (request.method == "POST"):
        title = request.form['title']
        text = request.form['noteText']
        from datetime import date
        today = date.today()
        today = today.strftime("%m-%d-%Y")
        id = len(notes) + 1
        notes[id] = {'title': title, 'text': text, 'date': today}
        return redirect(url_for('get_notes', name=a_user))
    else:
        return render_template('new.html', user=a_user)


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=False)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.
