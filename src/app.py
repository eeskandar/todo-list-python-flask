from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    todos_json = jsonify(todos)
    return todos_json

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position-1)
    todos_json = jsonify(todos)
    return todos_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)


"""
@app.route('/todos', methods=['GET', 'POST'])
if request.method == 'GET'
    def hello_world():
        json_todos = jsonify(todos)
        return json_todos

if request.method == 'POST'
    def add_new_todo():
        request_body = request.data
        print("Incoming request with the following body ", resquest_body)
        return 'Response for the POST todo'
"""