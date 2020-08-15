import secrets
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

from perswebs import routes
