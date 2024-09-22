from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://ratie:c9ydQe0B0YYiGNo4@jibulant-octo-enigma.qzu5j.mongodb.net/?retryWrites=true&w=majority&appName=jibulant-octo-enigma"

# MongoDB connection setup
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
#client = MongoClient(uri, server_api=ServerApi('1'))

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

# song = {
#         "artist": "Nipsey Hussle",
#         "lyrics": "[Intro: Stacy Barthe & Arctic Monkeys]\nWoah-oh\nWoah-oh\nWoah-oh\nLike the beginning of Mean Streets, you could (Oh)\nLike the beginning of Mean Streets, you could\nLike the beginning of Mean Streets, you could\n\n[Verse 1: Nipsey Hussle & Arctic Monkeys]\nI'm prolific, so gifted\nI'm the type that's gon' go get it, no kiddin'\nBreaking down a Swisher front of your buildin'\nSitting on the steps, feeling no feelings\nLast night, it was a cold killin'\nYou gotta keep the devil in his hole, nigga\nBut you know how it go, nigga\nI'm front line every time it's on, nigga\nHunnid proof flow, run and shoot pro\n458 drop, playin' \"Bullet Proof Soul\"\nEvery few shows, I just buy some new gold\nCircle got smaller, everybody can't go\nDowntown, Diamond District, jewelers like, \"Yo\nHussle, holla at me, I got Cubans on the low\"\nFlew to Cancun, smokin' Cubans on the boat\nThen docked at Tulum just to smoke, look\nListening to music at the Mayan Ruins\nTrue devotion on the bluest ocean, cruisin'\nMy cultural influence even rival Lucien\nI'm integrated vertically, y'all niggas blew it\nThey tell me, \"Hussle, dumb it down, you might confuse 'em\"\nThis ain't that weirdo rap you motherfuckers used to\nLike the beginning of Mean Streets\nI'm an urban legend, South Central in a certain section\nCan't express how I curved detectives\nGuess it's evidence of a divine presence, blessings\nHeld me down, at times, I seem reckless, F it\nYou got an L, but got an E for effort, stretched him\nDropped him off in the Mojave desert, then left him\nAin't no answer to these trick questions\nMoney Makin' Nip, straighten out my jewelry on my bitch dresser\nWell known, flick up and jail pose\nSnatch a champagne bottle from Rico's 'til T show\nWhatever, nigga, playin' chess, not checkers, nigga\nThirty-eight special for you clever niggas\nSee, bro, if you ain't live and die by the street code\nBeen through all these motions, up and down like a see-saw\nI can never view you as my equal\nFuck I wanna hear your CD for?\n",
#         "title": "Victory Lap by Nipsey Hussle (Ft. Stacy Barthe)",
#         "url": "https://genius.com/Nipsey-hussle-victory-lap-lyrics"
#     }
#
# save_song_to_mongodb(song)

