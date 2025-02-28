from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Function to load JSON data
def load_data():
    json_path = os.path.join(app.root_path, "static", "data.json")
    with open(json_path) as f:
        return json.load(f)

@app.route("/")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/qualifications")
def coursework():
    return render_template("qualifications.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/healthmetrics")
def healthmetrics():
    return render_template("healthmetrics.html")

@app.route("/montecarlo")
def montecarlo():
    return render_template("montecarlo.html")

@app.route("/sleepanalysis")
def sleepanalysis():
    return render_template("sleepanalysis.html")

@app.route("/get_data")
def get_data():
    data = load_data()
    
    # Create a mapping: Courses -> Skills
    course_to_skills = {course: skills for course, skills in data["courses"].items()}

    # Create a mapping: Education Methods -> Skills (indirect via courses)
    education_to_skills = {}
    for method, courses in data["education_methods"].items():
        related_skills = set()
        for course in courses:
            if course in course_to_skills:
                related_skills.update(course_to_skills[course])
        education_to_skills[method] = list(related_skills)

    # Return structured data including all mappings
    return jsonify({
        "education_methods": data["education_methods"],
        "courses": data["courses"],
        "education_to_skills": education_to_skills
    })

if __name__ == "__main__":
    app.run(debug=True)