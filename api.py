from flask import Flask,jsonify
app = Flask(__name__)

tasks = [
    {
        'id':1,
        'task':'this is first task'
    },
    {
        'id':2,
        'task':'this is another task'
    }
]

@app.route('/app-name/api/v0.1/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})  #will return the json

if(__name__ == '__main__'):
    app.run(debug = True)