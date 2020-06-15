from SpotifySentimentMap import app
from SpotifySentimentMap.functions import SpotifyClient
from flask import render_template, url_for, redirect, request, session

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
spotify = SpotifyClient(CLIENT_ID, CLIENT_SECRET)


@app.route('/')
def spotify_auth():
    return redirect(spotify.get_auth_url())


@app.route("/callback")
def callback():
    spotify.get_access_token()
    return redirect(url_for('home'))

@app.route("/home")
def home():
    if spotify.access_token != None:
        return render_template('index.html', title="We did it!")
    return render_template('index.html')