from habittracker import db


class Habit(db.Model):  # type: ignore[name-defined]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Habit('{self.name}', '{self.desc}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    habits = db.relationship('Habit', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
