import lyricsgenius
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

genius = lyricsgenius.Genius("X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY")
nltk.download('vader_lexicon')

def clean_lyrics(lyrics):
    """
    Cleans up the song lyrics by removing any blank lines and leading/trailing whitespace.
    """
    lines = lyrics.split('\n')
    lines = lines[1:]
    lyrics_lines = [line.strip() for line in lines if line.strip()]
    cleaned_lyrics = ' '.join(lyrics_lines)
    return cleaned_lyrics

def get_sentiment_score(text):
    """
    Analyzes the sentiment of the given text and returns a sentiment score.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

def main():
    song_input = input("Please type the name of the song you would like to analyze: ")
    song_search = genius.search_song(song_input)
    if song_search:
        lyrics = song_search.lyrics
        cleaned_lyrics = clean_lyrics(lyrics)
        sentiment_score = get_sentiment_score(cleaned_lyrics)
        if sentiment_score['compound'] >= 0:
            print(f"{song_search.title} has a happy sentiment score.")
            # Add song to happy playlist
        else:
            print(f"{song_search.title} has a sad sentiment score.")
            # Add song to sad playlist
    else:
        print(f"Sorry, couldn't find the lyrics for {song_input} on Genius. Please try again.")

if __name__ == '__main__':
    main()