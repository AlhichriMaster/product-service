"""
Product Service - Python Implementation
Complies with 12-Factor App Methodology (Factors 1-4)
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)

# Factor III: Config - Store config in the environment
# Fetch the port from environment variables or default to 3030
PORT = int(os.getenv('PORT', '3030'))

# Factor IV: Backing Services - Treat backing services as attached resources
# (In this simple case, we're using in-memory data, but the structure supports
# easy replacement with a database connection via environment variables)

# Configure CORS to allow requests from any origin
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET"]}})


@app.route('/products', methods=['GET'])
def get_products():
    """
    GET /products endpoint
    Returns a JSON array of product objects
    """
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for container orchestration
    """
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    # Factor I: Codebase - One codebase tracked in revision control, many deploys
    # This app should be tracked in Git with a single codebase
    
    # Factor II: Dependencies - Explicitly declare and isolate dependencies
    # Dependencies are declared in requirements.txt
    
    # Run the application
    # Bind to 0.0.0.0 to allow external connections (important for Docker)
    app.run(host='0.0.0.0', port=PORT, debug=False)
