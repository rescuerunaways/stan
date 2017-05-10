import os

from flask import Flask


app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

from app.controllers import payload
from app.errors import err_handlers