from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


app= Flask(__name__)
app.config.from_object(Config)

# The next line is for the inclusion of Flask Bootstrap
Bootstrap(app)


from application import routes