from flask import Flask, request, jsonify
from flask_cors import CORS
from redmine_driver import RedmineDriver
import os

app = Flask(__name__)
CORS(app)
FORMAT = '%H:%M'


@app.route("/register", methods=['POST'])
def register_hours():
    task_list = request.json
    print(task_list)
    driver = RedmineDriver()
    driver.login(os.environ.get("REDMINE_USERNAME"), os.environ.get("REDMINE_PASSWORD"))

    for task in task_list:
        driver.register_task(task['time'], task['comment'], task['task'], task['date'])

    driver.close()
    return "Hours Registered."