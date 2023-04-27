import requests
from bs4 import BeautifulSoup
import nltk
import urllib.request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import lyricsgenius
import pandas as pd
import re

genius = lyricsgenius.Genius(
    "X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY"
)


def song_search_function():
    songs = {}
    songs_added = 0
    i=0
    while i != 1:
        i = 0
        song_input = input(
            "Please type the name of the song you would like to add: ")

        song_search = genius.search_song(song_input)

        if song_search:
            songs[song_search.title] = song_search.lyrics
            songs_added += 1
        else:
            print(f"{song_input} couldn't be found on Genius. Please try again.")
       
        i = input("\nWould you like to add another song?")
        i = i.lower()
        if i == "yes":
            i = 0
        else:
            i = 1
            return songs

def clean_lyrics(songs):
    for title,lyrics in songs.items():
        lines = lyrics.split('\n')
        lines = lines[1:]
        lyrics_lines = [line.strip() for line in lines if line.strip()]
        lyrics = ' '.join(lyrics_lines)
        songs[title] = lyrics
    return songs


def main():
    songs_dict = song_search_function()
    songs_dict = clean_lyrics(songs_dict)
    print(songs_dict)


if __name__ == '__main__':
    main()


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
