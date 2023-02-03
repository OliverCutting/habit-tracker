from habittracker import db


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_name = db.Column(db.String(30), unique=True, nullable=False)
    habit_desc = db.Column(db.String())

    def __repr__(self):
        return f"Habit('{self.habit_name}', '{self.habit_desc}')"
