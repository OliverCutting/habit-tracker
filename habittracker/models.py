from habittracker import db


class Habit(db.Model):  # type: ignore[name-defined]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    desc = db.Column(db.String())

    def __repr__(self):
        return f"Habit('{self.name}', '{self.desc}')"
