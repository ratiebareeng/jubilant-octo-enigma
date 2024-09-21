# Make HTTP Requests
import requests

# Scrape data from HTML Document
from bs4 import BeautifulSoup

# I/O
import os

# Search and manipulate strings
import re

import csv

import pandas

import json

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

        # Collect song info from song objects
        for song in song_info:
            if len(songs) < song_cap:
                url = song['result']['url']
                artist = artist_name
                song_title = song['result']['full_title']

                songs.append({
                              'artist': artist,
                              'title': song_title,
                              'url': url,
                              })

        if len(songs) == song_cap:
            break
        else:
            page += 1
    #print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs


# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')

    for br in html.select("br"):
        br.replace_with("\n")

    html = html.find('div', class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')

    lyrics = html.get_text()

    return lyrics


def lyrics(song_url=None, remove_section_headers=False):
    """Uses BeautifulSoup to scrape song info off of a Genius song URL
    Args:
        song_url (:obj:`str`, optional): Song URL.
        remove_section_headers (:obj:`bool`, optional):
            If `True`, removes [Chorus], [Bridge], etc. headers from lyrics.
    Returns:
        :obj:`str` \\|‌ :obj:`None`:
            :obj:`str` If it can find the lyrics, otherwise `None`
    Note:
        If you pass a song ID, the method will have to make an extra request
        to obtain the song's URL and scrape the lyrics off of it. So it's best
        to pass the method the song's URL if it's available.
        If you want to get a song's lyrics by searching for it,
        use :meth:`Genius.search_song` instead.
    Note:
        This method removes the song headers based on the value of the
        :attr:`Genius.remove_section_headers` attribute.
    """
    msg = "Please provide `song_url`."
    assert None not in ([song_url]), msg

    # Scrape the song lyrics from the HTML
    page = requests.get(song_url)
    html = BeautifulSoup(page.text, 'html.parser')

    #     (
    #     BeautifulSoup(
    #     self._make_request(path, web=True).replace('<br/>', '\n'),
    #     "html.parser"
    # ))
    # Determine the class of the div
    divs = html.find_all("div", class_=re.compile("^lyrics$|Lyrics__Container"))
    if divs is None or len(divs) <= 0:
        print("Couldn't find the lyrics section. "
              "Please report this if the song has lyrics.\n"
              f"Song URL: {song_url}")
        return None

    html.find_all("div", class_=re.compile("^lyrics$|Lyrics__Container"))
   # ("br", lyricsContainer).replaceWith("\n")
    lyricsContainer = html.find("Lyrics__Container-sc-1ynbvzw-1 kUgSbL")

    lyrics_string = "\n".join([div.g.get_text("\n") for div in divs])
    # Remove [Verse], [Bridge], etc.
    # if self.remove_section_headers or remove_section_headers:
    #     lyrics = re.sub(r'(\[.*?\])*', '', lyrics)
    #     lyrics = re.sub('\n{2}', '\n', lyrics)  # Gaps between verses
    return lyrics_string.replace("\n", " ")


def check_value(data, val):
    return any(player['steam64']==val for player in data['players'])


def write_lyrcis_to_file(song):
    csv_file = open(f"{song['artist']}_lyrics.csv", 'a', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['Artist', 'Title', 'URL', 'Lyrics'])
    df = pandas.read_csv(f'{song['artist']}_lyrics.csv')

    if df['Title'].eq(song['title']).any():
        print(f'{song['title']} already exists')
    else:
        writer.writerow(song.values())
        csv_file.close()


def write_lyrics_to_json(song_to):
    song_json_object = json.dumps(song_to, indent=4)
    song_url = song_to['artist'].replace(' ', '_')
    file_name = song_url+'.json'

    with open(file_name, 'a+') as outfile:
        artist_data = outfile.read()

        #if song_to['url'] not in artist_data:
        if artist_data.__contains__(song_to['url']):
            print(f"{song_to['title']} already exists")
        else:
            outfile.write(song_json_object)

