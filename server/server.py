from flask import Flask, request, jsonify
from flask_cors import CORS
from redmine_driver import RedmineDriver
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)
FORMAT = '%H:%M'


@app.route("/register", methods=['POST'])
def register_hours():
    task_json = request.json
    driver = RedmineDriver()
    driver.login(os.environ.get("REDMINE_USERNAME"), os.environ.get("REDMINE_PASSWORD"))

    tasks = [{
        'date': datetime.strptime(task['date'], "%Y-%m-%d"),
        'time': task['time'].strip(), 
        'task': task['task'].strip(),
        'comment': task['comment'].strip(),
    } for task in task_json]
    print(tasks)

    for task in tasks:
        driver.register_task(task['time'], task['comment'], task['task'], task['date'])

    
    driver.syncronize_tasks_mongo(os.environ.get("MONGO_CONNECTION"), tasks)

    driver.close()
    return "Hours Registered."