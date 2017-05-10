import os

from flask import Flask

app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))
app.config['DEBUG'] = True

from app.controllers import payload
from app.errors import err_handlers

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
