from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def index():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Buzz')


@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)