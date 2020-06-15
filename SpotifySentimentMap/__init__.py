from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

from SpotifySentimentMap import routes