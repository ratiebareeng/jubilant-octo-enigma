import requests
from bs4 import BeautifulSoup
import json


def clean_lyricsh(lyrics):
    # Remove backslashes
    lyrics = lyrics.replace('\\', '')

    # Remove extra quotes from the start and end of the lyrics
    lyrics = lyrics.strip('\"')

    # Remove quotes around lines if they are enclosed in quotes
    cleaned_lines = []
    for line in lyrics.split('\n'):
        cleaned_line = line.strip('\"')
        cleaned_lines.append(cleaned_line)

    return '\n'.join(cleaned_lines)


def clean_lyrics2(lyrics):
    # Remove backslashes used to escape quotes
    lyrics = lyrics.replace('\\', '')

    # Remove extra quotes from the start and end of the lyrics
    lyrics = lyrics.strip('\"')

    # Remove quotes around lines if they are enclosed in quotes
    cleaned_lines = []
    for line in lyrics.split('\n'):
        # Strip leading and trailing quotes, and any trailing spaces
        cleaned_line = line.strip('\"').strip()
        cleaned_lines.append(cleaned_line)

    return '\n'.join(cleaned_lines)


def clean_lyrics(lyrics):
    lyrics = lyrics.replace('\\', '')
    lyrics = lyrics.strip('\"')
    cleaned_lines = [line.strip('\"') for line in lyrics.split('\n')]
    return '\n'.join(cleaned_lines)


def scrape_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract lyrics
    lyrics_div = soup.find('div', {'data-lyrics-container': 'true', 'class': 'Lyrics__Container-sc-1ynbvzw-1'})
    if lyrics_div:
        lyrics = lyrics_div.get_text(separator='\n').strip()
        lyrics = clean_lyrics(lyrics)
    else:
        lyrics = "Lyrics not found"

    # Extract song and artist details
    details_div = soup.find('div', class_='SongHeaderdesktop__SongDetails-sc-1effuo1-5 dhqXbj')
    if details_div:
        title_tag = details_div.find('h1')
        artist_tag = details_div.find('a')
        title = title_tag.text.strip() if title_tag else "Unknown Title"
        artist = artist_tag.text.strip() if artist_tag else "Unknown Artist"
    else:
        title = "Unknown Title"
        artist = "Unknown Artist"

    # Extract release date
    release_date_div = details_div.find('div', class_='MetadataStats__Container-sc-1t7d8ac-0 cDJyol')
    if release_date_div:
        release_date_tag = release_date_div.find('div', class_='LabelWithIcon__Container-hjli77-0 gcYcIR')
        if release_date_tag:
            release_date = release_date_tag.get_text().strip()
        else:
            release_date = "Unknown Date"
    else:
        release_date = "Unknown Date"

    # Create JSON structure
    lyrics_json = {
        "title": title,
        "artist": artist,
        "album": "Unknown Album",  # Placeholder if album extraction isn't updated yet
        "release_date": release_date,
        "lyrics": lyrics.split('\n')
    }

    return lyrics_json


# Example usage
url = "https://genius.com/Nipsey-hussle-victory-lap-lyrics"
result = scrape_lyrics(url)
print(json.dumps(result, indent=2))