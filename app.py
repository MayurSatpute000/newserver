from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Deployment successful! The server is running smoothly.",
        "environment": "production"
    })

if __name__ == '__main__':
    # Binding to 0.0.0.0 is required for the phone to expose the port to the internet
    app.run(host='0.0.0.0', port=5000)