"""
SPOTIFY SENTIMENT MAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Creating a Spotify Sentiment Map using the recently heard
music, song lyrics, bpm, and artist previous genre. Should
result in a word map on a web page.
"""

from SpotifySentimentMap import app

# run the app
if __name__ == '__main__':
    app.run(debug=True)
