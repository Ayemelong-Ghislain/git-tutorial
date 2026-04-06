from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Blockchain Voting System</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0; }
            h1 { color: #2c3e50; }
            button { padding: 15px 30px; margin: 10px; font-size: 18px; cursor: pointer; background: #3498db; color: white; border: none; border-radius: 8px; }
            button:hover { background: #2980b9; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 16px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🗳️ Blockchain Voting System</h1>
            <p>Your voting system is running on Render!</p>
            <div>
                <button onclick="alert('Voted for Alice')">Vote for Alice</button>
                <button onclick="alert('Voted for Bob')">Vote for Bob</button>
                <button onclick="alert('Voted for Charlie')">Vote for Charlie</button>
            </div>
            <p id="status" style="color: green; margin-top: 20px;">✅ System Online</p>
        </div>
    </body>
    </html>
    '''

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'message': 'Voting system is live!'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
