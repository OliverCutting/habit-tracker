from flask import flash, redirect, render_template, request, url_for
from habittracker import app, db, bcrypt
from habittracker.forms import HabitInputForm, RegistrationForm, LoginForm
from habittracker.models import Habit, User
from flask_login import login_user, logout_user, current_user, login_required


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


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You may now login", "success")
        return redirect(url_for("login"))
    return render_template(
        "register.html", title="Register", form=form, legend="Register"
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("dashboard"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form, legend="Login")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("dashboard"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="My Account", Legend="My Account")


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
    return redirect(url_for("dashboard"))
