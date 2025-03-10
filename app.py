# app.py
from flask import Flask, send_from_directory, jsonify

# Create a Flask app with static folder set to 'static'
app = Flask(__name__, static_folder='static')

# Route to serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Simple API endpoint that returns a JSON response
@app.route('/api')
def api():
    return jsonify({'message': 'Hello from Flask API!'})

if __name__ == '__main__':
    # Listen on all interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)
