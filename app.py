import config
from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import HabitInputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
app.app_context().push()


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_name = db.Column(db.String(30), unique=True, nullable=False)
    habit_desc = db.Column(db.String())

    def __repr__(self):
        return f"Habit('{self.habit_name}', '{self.habit_desc}')"


habits = [
    {"name": "Drink Water", "desc": "2l a day"},
    {"name": "Workout", "desc": "Lift weights"},
]


@app.route("/test")
def hello_world():
    return "Flask is working"


@app.route("/")
def home():
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", habits=habits, title="My Dashboard")


@app.route("/createhabit", methods=["GET", "POST"])
def create_habit():
    form = HabitInputForm()
    if form.validate_on_submit():
        flash("Habit Created!", "success")
        habits.append({"name": form.habit_name.data, "desc": form.habit_desc.data})
        return redirect(url_for("dashboard"))

    return render_template("create_habit.html", title="Creat Habit", form=form)


if __name__ == "__main__":
    app.run()
