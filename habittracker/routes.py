from habittracker import app, db
from habittracker.forms import HabitInputForm
from habittracker.models import Habit
from flask import flash, redirect, render_template, url_for


@app.route("/test")
def hello_world():
    return "Flask is working"


@app.route("/")
def home():
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    habits = Habit.query.all()
    return render_template("dashboard.html", habits=habits, title="My Dashboard")


@app.route("/habit/new", methods=["GET", "POST"])
def create_habit():
    form = HabitInputForm()
    if form.validate_on_submit():
        habit = Habit(name=form.name.data, desc=form.desc.data)
        db.session.add(habit)
        db.session.commit()
        flash("Habit Created!", "success")
        return redirect(url_for("dashboard"))

    return render_template("create_habit.html", title="Create Habit", form=form)


@app.route("/habit/<int:habit_id>", methods=["GET", "POST"])
def habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    return render_template("habit.html", title=habit.name, habit=habit)
