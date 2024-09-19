from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app, resources={r"/receive": {"origins": "http://localhost:3000"}})

logging.basicConfig(level=logging.DEBUG)

@app.route('/receive', methods=['POST', 'OPTIONS'])
def receive_data():
    app.logger.info(f"Received request: {request.method}")
    app.logger.info(f"Request headers: {request.headers}")
    
    if request.method == 'OPTIONS':
        return jsonify({"status": "success", "message": "CORS preflight request successful"}), 200

    if request.method == 'POST':
        app.logger.info(f"Request body: {request.get_data(as_text=True)}")
        try:
            data = request.json
            app.logger.info(f"Received data: {data}")
            return jsonify({"status": "success", "message": "Data received by Python server"})
        except Exception as e:
            app.logger.error(f"Error processing request: {str(e)}")
            return jsonify({"status": "error", "message": "Error processing request"}), 400
    else:
        return jsonify({"status": "error", "message": "Method not allowed"}), 405

@app.errorhandler(405)
def method_not_allowed(error):
    app.logger.error(f"Method not allowed: {request.method}")
    return jsonify({"status": "error", "message": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(port=5000, debug=True)
