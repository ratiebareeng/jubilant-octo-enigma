from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#import certifi

uri = "mongodb+srv://ratie:c9ydQe0B0YYiGNo4@jibulant-octo-enigma.qzu5j.mongodb.net/?retryWrites=true&w=majority&appName=jibulant-octo-enigma"

# MongoDB connection setup
# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
client = MongoClient(uri, server_api=ServerApi('1'))

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
