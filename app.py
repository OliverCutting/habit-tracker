import config
from flask import Flask, flash, redirect, render_template, url_for
from forms import HabitInputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY

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
