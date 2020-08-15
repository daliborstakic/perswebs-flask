import secrets
from flask import Flask

app = Flask(__name__)
# Secret hex key
app.config['SECRET_KEY'] = secrets.token_hex(16)

# Importing the routes module
from perswebs import routes
