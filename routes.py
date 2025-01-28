from flask import Flask, redirect, render_template, request, Blueprint, url_for
from collections import defaultdict
import datetime
import uuid

# Initialize Flask app
app = Flask(__name__)

# Set up Blueprint
pages = Blueprint("habits", __name__, template_folder="templates", static_folder="static")

# Mock data structures
habits = ["Test habit"]
completions = defaultdict(list)

# Context processor to add date_range function to templates
@pages.context_processor
def add_calc_date_range():
    def date_range(start: datetime.datetime):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates
    return {"date_range": date_range}

# Route for the home page
@pages.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.datetime.fromisoformat(date_str)
    else:
        selected_date = datetime.datetime.today()

    # Fetch habits and completions from the database (mock logic for now)
    habits_on_date = habits  # Replace with actual database query
    completions_on_date = completions.get(selected_date, [])

    return render_template(
        "index.html",
        title="Habit Tracker - Home",
        selected_date=selected_date,
        habits=habits_on_date,
        completions=completions_on_date,
    )

# Route to add a new habit
@pages.route("/add", methods=["GET", "POST"])
def add_habit():
    today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    if request.method == "POST" and request.form.get("habit"):
        habit_name = request.form.get("habit")
        habits.append(habit_name)  # Replace with actual database insertion logic
        return redirect(url_for("habits.index"))

    return render_template(
        "add_habit.html",
        title="Habit Tracker - Add Habit",
        selected_date=datetime.datetime.today(),
    )

# Route to mark a habit as completed
@pages.route("/complete", methods=["POST"])
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habitName")
    date = datetime.datetime.fromisoformat(date_string)
    completions[date].append(habit)  # Replace with actual database insertion logic

    return redirect(url_for("habits.index", date=date_string))

# Register Blueprint with the app
app.register_blueprint(pages)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)