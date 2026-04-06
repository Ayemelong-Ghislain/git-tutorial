from flask import Flask, render_template, jsonify
from web3 import Web3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'message': 'Voting system is live!'
    })

@app.route('/api/candidates')
def candidates():
    return jsonify({
        'candidates': ['Alice', 'Bob', 'Charlie'],
        'votes': [0, 0, 0]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
