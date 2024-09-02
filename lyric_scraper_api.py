from flask import Flask, request, jsonify
from lyric_scraper import scrape_lyrics  # Ensure you have this module

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


if __name__ == '__main__':
    app.run(debug=True)
