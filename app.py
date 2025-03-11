from flask import Flask, send_from_directory, jsonify

# Set the static folder to "static" (which is /app/static)
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    # Serve the index.html from the root folder (/app/index.html)
    return send_from_directory('.', 'index.html')

@app.route('/api')
def api():
    return jsonify({'message': 'Hello from Flask API!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

