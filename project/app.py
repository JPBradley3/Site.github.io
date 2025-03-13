from flask import Flask, render_template, json
import requests  # Correctly import requests for making API calls
import os

app = Flask(__name__)

def load_resume():
    """Loads resume data from JSON file"""
    json_path = os.path.join("data", "indeed_resume.json")
    with open(json_path, "r") as file:
        return json.load(file)

def get_github_repositories():
    """Fetches repository data from GitHub API"""
    github_username = "JPBradley3"
    url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(url)  # Use requests to fetch data
    if response.status_code == 200:
        return response.json()  # Return the repository data as a JSON list
    else:
        return []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    repositories = get_github_repositories()  # Get GitHub repositories
    return render_template("projects.html", repositories=repositories)

@app.route("/resume")
def resume():
    resume_data = load_resume()
    return render_template("resume.html", resume=resume_data)

if __name__ == "__main__":
    app.run(debug=True)
