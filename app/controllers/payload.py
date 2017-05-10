from flask import request as req

from app import app
from app.services.processor import process
from flask import jsonify


@app.route('/payload', methods=['POST'])
def process_payloads():
    return jsonify(process(req.data))
