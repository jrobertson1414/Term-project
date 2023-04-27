import requests
from bs4 import BeautifulSoup
import nltk
import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import lyricsgenius
import pandas as pd

genius = lyricsgenius.Genius(
    "X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY"
)


def song_search_function():
    songs = {}
    songs_added = 0

    while songs_added < 3:
        song_input = input("Please type the name of the song you would like to add: ")

        song_search = genius.search_song(song_input)

        if song_search:
            songs[song_search.title] = song_search.lyrics
            songs_added += 1
        else:
            print(f"{song_input} couldn't be found on Genius. Please try again.")
    return songs


songs_dict = song_search_function()
print(songs_dict)


# for artist in artists:
#     # Get the artist object
#     artist_obj = genius.search_artist(artist, max_songs=1)

#     # Print the artist name
#     print(artist_obj.name)

#     # Loop through the artist's songs and print the lyrics
#     for song in artist_obj.songs:
#         print(song.lyrics)


# artist = genius.search_artist("Sigala", max_songs=3, sort="title")
# print(artist.songs)


# sentiment_analyzer = SentimentIntensityAnalyzer()

# Genius_api_key = 'X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
# headers = {
#     'Authorization': 'Bearer X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
# }
# response = requests.get('https://api.genius.com/songs/378195', headers=headers)

# def download_page(url):
#     return urllib.request.urlopen(url)


# def parse_html(html):
#     """
#     Analyze the genius top 50 songs page, find the information and return the song and lyrics list of tuples
#     (song_name, lyrics)
#     """
#     soup = BeautifulSoup(response.text, "html.parser")
#     print(soup.prettify())

# lyrics_finder = soup.find("div", class_="lyrics")
# lyrics = lyrics_finder.text.strip()


# The thing about sentiment analysis is that there is only positive, negative, and neutral. We could technically create our own genres by maybe saying that neutral lyrics are "chill"
# or maybe we can combine the bpm and the sentiment analysis to determine that. For example, songs with bpm over 100 are usually pretty upbeat, and slower songs under 100 bpm
# have a higher likelihood of being negative/ neutral


# Original Code

# data = response.json()
# print(data)
# title = data['response']['song']['title']
# print(title)
