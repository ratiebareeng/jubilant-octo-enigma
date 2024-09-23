from crypt import methods

from flask import Flask, request, jsonify

from db_connection import save_songs_to_mongodb
from lyric_scraper import scrape_lyrics # Ensure you have this module
from scraper import  request_song_url, scrape_song_lyrics

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        result = scrape_lyrics(url)  # Call your scraping function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Scrape artist songs
@app.route('/scrapeArtist', methods=['POST'])
def scrape_artist():
    data = request.get_json()
    artist_name = data.get('artistName')
    songCap = data.get('songCap')
    if not artist_name:
        return  jsonify({'error': 'Artist Name is required'}), 400
    if not songCap:
        songCap = 10

    try:
        songs = request_song_url(artist_name, songCap)

        for song in songs:
            song['lyrics'] = scrape_song_lyrics(song['url'])

        save_songs_to_mongodb(songs)

        return jsonify(songs)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
