# Make HTTP Requests
import requests

# Scrape data from HTML Document
from bs4 import BeautifulSoup

# I/O
import os

# Search and manipulate strings
import re

GENIUS_API_TOKEN = 'XadGUaIEgDRc37TPpYQXbB7VaJh6sy89o21V5n0e2SRlsmmBDum1Zt90bbOFAsN7'

# Get a list of Genius.com URL’s for a
# specified number of songs for an artist


# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []

    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()

        # Collect up to song_cap song objects from artist
        song_info = []
        for hit in json['response']['hits']:
            if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
                song_info.append(hit)

        # Collect song URL's from song objects
        for song in song_info:
            if len(songs) < song_cap:
                url = song['result']['url']
                songs.append(url)

        if len(songs) == song_cap:
            break
        else:
            page += 1
    print('Found {} songs by {}'.format(len(songs), artist_name))
    # print(songs)
    return songs


request_song_url('Nipsey Hussle', 20)