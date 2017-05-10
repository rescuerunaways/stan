from json import dumps

from app import app

@app.errorhandler(Exception)
def all_exception_handler(error):
    return dumps({"error": "Could not decode request: JSON parsing failed"}), 400

