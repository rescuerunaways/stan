from flask import jsonify

from app import app


@app.errorhandler(Exception)
def all_exception_handler(error):

    return jsonify({"error": "Could not decode request: JSON parsing failed"}), 400

