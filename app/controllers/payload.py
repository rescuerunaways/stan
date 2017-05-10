from flask import request as req

from app import app
from app.services.processor import process


@app.route('/payloads', methods=['POST'])
def process_payloads():
    return process(req.data)

