from flask import Flask, render_template
app = Flask(__name__)

habits = [
  {
    'name': 'Drink Water',
    'desc': '2l a day'
  },
  {
    'name': 'Workout',
    'desc': 'Lift weights'
  }
]

@app.route("/test")
def hello_world():
  return "Flask is working"

@app.route("/")
@app.route("/dashboard")
def dashboard():
  return render_template('dashboard.html', habits=habits, title='My Dashboard')

if __name__ == '__main__':
  app.run()