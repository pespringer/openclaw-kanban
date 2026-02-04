# Python Application: Kanban Project Management Board
# Ollama-generated initial draft

import json
from flask import Flask, jsonify, request

app = Flask(__name__)

data_file = "tasks.json"

def load_tasks():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(data_file, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    task_data = request.json
    tasks = load_tasks()
    tasks.append(task_data)
    save_tasks(tasks)
    return jsonify({"message": "Task added successfully"}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task_data = request.json
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id].update(task_data)
        save_tasks(tasks)
        return jsonify({"message": "Task updated successfully"})
    return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
        return jsonify({"message": "Task deleted successfully"})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)