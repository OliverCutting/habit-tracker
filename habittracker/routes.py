from habittracker import app, db
from habittracker.forms import HabitInputForm
from habittracker.models import Habit
from flask import flash, redirect, render_template, request, url_for


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

    return render_template(
        "create_habit.html", title="Create Habit", form=form, legend="Update Post"
    )


@app.route("/habit/<int:habit_id>", methods=["GET", "POST"])
def habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    return render_template("habit.html", title=habit.name, habit=habit)


@app.route("/habit/<int:habit_id>/update", methods=["GET", "POST"])
def update_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    form = HabitInputForm()
    if form.validate_on_submit():
        habit.name = form.name.data
        habit.desc = form.desc.data
        db.session.commit()
        flash("Habit Updated!", "success")
        return redirect(url_for("habit", habit_id=habit.id))
    elif request.method == "GET":
        form.name.data = habit.name
        form.desc.data = habit.desc
    return render_template(
        "create_habit.html", title="Update Habit", form=form, legend="Update Habit"
    )


@app.route("/habit/<int:habit_id>/delete", methods=["POST"])
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    db.session.delete(habit)
    db.session.commit()
    flash("Habit Deleted!", "success")
    return redirect(url_for('dashboard'))