import csv
import json

import pandas


def write_to_csv(song):
    """Uses csv to write song info to a csv file
    Args:
        song (:obj:`str`, optional): Song.

    Returns:
        :param song:
        :obj:`str` :obj:`None`:
            :obj:`str` Path to the location of the file,
            if it can write to the file, otherwise `None`
    Note:
        A note
    Note:
        Another note
    """
    msg = "Please provide the `song` to extract the lyrics from."
    assert None not in ([song]), msg

    csv_file = open(f'{song['artist']}_lyrics.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(['Artist', 'Title', 'URL', 'Lyrics'])
    df = pandas.read_csv(f'{song['artist']}_lyrics.csv')

    if df['Title'].eq(song['title']).any():
        print(f'{song['title']} already exists')
    else:
        writer.writerow(song.values())
        csv_file.close()


def write_to_json(songs):
    """Uses json to write song info to a json file
    Args:
        song (:obj:`str`, required): Song.

    Returns:
        :param song:
        :obj:`str` :obj:`None`:
            :obj:`str` Path to the location of the file,
            if it can write to the file, otherwise `None`
    Note:
        A note
    Note:
        Another note
    """
    msg = "Please provide the `song` to extract the lyrics from."
    assert None not in ([songs]), msg

    songs_json_object = json.dumps(songs, indent=4)
    song_url = songs['artist'].replace(' ', '_')
    file_name = song_url+'.json'

    with open(file_name, 'a+') as outfile:
        artist_data = outfile.read()

        number_of_songs_to_add = 0
        for song in songs:
            # if song_to['url'] not in artist_data:
            if artist_data.__contains__(song['url']):
                print(f'{song['title']} already exists')
                print(f'{song['title']} will be removed from write list')
                songs.remove(song)
            else:
                number_of_songs_to_add += 1

        outfile.write(songs_json_object)
        print(f'{number_of_songs_to_add} songs scraped')
        #outfile.write(',')


# function to add to JSON
#def write_json(new_data, filename='data.json'):
def write_json(song):
    song_url = song['artist'].replace(' ', '_')
    file_name = song_url+'.json'
    #open(file_name, 'w').close()


    try:
        with open(file_name, mode='w+', encoding='utf-8') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            print('S T A R T 1')
            # Join new_data with file_data inside emp_details
            file_data.append(song)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent=4)
            print('D O N E')
    except Exception as error:
        print(error)

    # python object to be appended


