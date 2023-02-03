from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class HabitInputForm(FlaskForm):
    habit_name = StringField(
        "Habit Name", validators=[DataRequired(), Length(min=2, max=30)]
    )
    habit_desc = StringField("Habit Description")
    submit = SubmitField("Create Habit")
