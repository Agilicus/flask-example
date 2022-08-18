import flask
from flask_cors import CORS
from flask import jsonify

app = flask.Flask('app')
CORS(app)
app.config["DEBUG"] = True

@app.route('/api', methods=['GET'])
def stats():
    #Access-Control-Allow-Origin' header
    return jsonify({ 'status': True })

@app.route('/', methods=['GET'])
def home():
    return "NOT A WEB PAGE", 404

app.run('0.0.0.0', 5001)
