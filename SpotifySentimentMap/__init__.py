from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'

from SpotifySentimentMap import routes