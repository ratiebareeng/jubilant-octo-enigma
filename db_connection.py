from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import requests
from bs4 import BeautifulSoup
import re

uri = "mongodb+srv://ratie:c9ydQe0B0YYiGNo4@jibulant-octo-enigma.qzu5j.mongodb.net/?retryWrites=true&w=majority&appName=jibulant-octo-enigma"

# MongoDB connection setup
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

#Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged Jubilant Octo Enigma deployment. Successfully connected to MongoDB!")
except Exception as e:
    print(f"Failed to connect to DB: \n{e}")

db = client['dev_lyrics_db']  # Database name
songs_collection = db['songs']  # This will be the collection where we store the songs


def save_song_to_mongodb(song):
    # Check if the song already exists in the database
    existing_song = songs_collection.find_one({'url': song['url']})

    if existing_song:
        print(f"{song['title']} already exists in the database")
    else:
        # Insert the song into the database
        result = songs_collection.insert_one(song)
        print(f"Saved {song['title']} to MongoDB with id: {result.inserted_id}")


# Your existing functions (request_artist_info, request_song_url, scrape_song_lyrics, lyrics) remain unchanged

# Modified main scraping loop
def scrape_artist_songs(artist_name, song_cap):
    songs = request_song_url(artist_name, song_cap)
    for song in songs:
        lyrics = scrape_song_lyrics(song['url'])
        song['lyrics'] = lyrics
        save_song_to_mongodb(song)


# Example usage
if __name__ == "__main__":
    artist_name = "Taylor Swift"  # Replace with the artist you want to scrape
    song_cap = 5  # Number of songs to scrape
    scrape_artist_songs(artist_name, song_cap)

