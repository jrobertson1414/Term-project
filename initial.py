import lyricsgenius

from nltk.sentiment.vader import SentimentIntensityAnalyzer

import re

genius = lyricsgenius.Genius(
    "X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY"
)


def search_song_lyrics():
    """
    Searches for song lyrics on Genius.com using the lyricsgenius library and returns a dictionary
    containing the song title and lyrics for all songs found.
    """
    songs = {}
    songs_added = 0
    while True:
        song_title = input("Please enter the title of the song: ")
        artist_name = input("Please enter the artist of the song: ")
        song_search = genius.search_song(song_title, artist_name)
        if song_search:
            print(
                f"Found the following song: {song_search.title} by {song_search.artist}"
            )
            confirm = input("Is this the correct song? (yes or no): ")
            if confirm.lower() == "yes":
                songs[song_search.title] = song_search.lyrics
                songs_added += 1
            else:
                print("Sorry, please try again.")
        else:
            print(
                f"Sorry, couldn't find the lyrics for {song_title} by {artist_name} on Genius. Please try again."
            )
        add_another_song = input(
            "\nWould you like to add another song? (yes or no) ")
        if add_another_song.lower() != "yes":
            break
    return songs


def clean_song_lyrics(songs):
    """
    Cleans up the song lyrics by removing any blank lines and leading/trailing whitespace.
    """
    for title, lyrics in songs.items():
        lines = lyrics.split("\n")
        lines = lines[1:]
        lyrics_lines = [line.strip() for line in lines if line.strip()]
        cleaned_lyrics = " ".join(lyrics_lines)
        songs[title] = cleaned_lyrics
    return songs


def get_sentiment_score(lyrics):
    """
    Uses the SentimentIntensityAnalyzer from the nltk library to calculate the sentiment score
    for the given lyrics.
    """
    sentiment_analyzer = SentimentIntensityAnalyzer()
    sentiment_score = sentiment_analyzer.polarity_scores(lyrics)
    return sentiment_score


def add_songs_to_playlist(songs_dict):
    """
    Adds songs to the happy or sad playlist based on their sentiment score and prints out the
    songs added to each playlist with the artist name.
    """
    happy_playlist = {}
    sad_playlist = {}

    for title, lyrics in songs_dict.items():
        sentiment_score = get_sentiment_score(lyrics)
        if sentiment_score["compound"] >= 0.5:
            # happy_playlist.append((title.lower(), lyrics))
            happy_playlist[title.lower()]= lyrics
        elif sentiment_score["compound"] <= 0.5:
            # sad_playlist.append((title.lower(), lyrics))
            sad_playlist[title.lower()]= lyrics

    print("Happy playlist:")
    for title, lyrics in happy_playlist.items():
        print(f"{title}")
    print()

    print("Sad playlist:")
    for title, lyrics in sad_playlist.items():
        print(f"{title}")
    print()
    return sad_playlist, happy_playlist

def plyrics(happy,sad):
    while True:
        playlist = input("Which playlist do you want to choose a song from?(happy or sad)")
        title = input("What is the name of the song?")

        if playlist.lower()=="happy":
            if title.lower() not in happy:
                print("The song you chose is not in your chosen playlist\n")
            else:
                print(f'The lyrics to {title} are {happy[title.lower()]}\n')
        elif playlist.lower()=="sad":
            if title.lower() not in sad: 
                print("The song you chose is not in your chosen playlist\n")
            else:
                print(f'The lyrics to {title} are {sad[title.lower()]}\n')
        else:
            print("Invalid playlist name\n")
        i = input("Would you like to know any more lyrics?(yes or no)\n")
        if i.lower()!='yes':
            break

                


def main():
    print("This is a program that takes the input of your favourite songs and their artists and then categorizes them into playlists.\n")
    while True:
        songs = search_song_lyrics()
        cleaned_songs = clean_song_lyrics(songs)
        sad, happy = add_songs_to_playlist(cleaned_songs)
        ans = input("Would you like to know the lyrics of any song from either playlist?(yes or no)\n")
        if ans.lower()=="yes":
            plyrics(happy,sad)
        print("Hope you enjoyed your playlists!")
        break


if __name__ == "__main__":
    main()