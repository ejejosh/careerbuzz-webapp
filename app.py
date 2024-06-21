from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def index():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)


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


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template("jobpage.html", listed_job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
