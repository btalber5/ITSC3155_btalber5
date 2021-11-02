from database import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.String(400), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

class User(db.Model):
    id =db.Column("id", db.Integer, primary_key = true)
    name = db.Column("name", db.String(100), nullable = false)
    email = db.Column("email", db.String(100), nullable = false)

    def __repr__(self):
        return '<Name> %r' % self.id
    def __init__(self, id, name, email):
        self.id = id
        self.name - name
        self.email = email