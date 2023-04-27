import requests
from bs4 import BeautifulSoup
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiment_analyzer = SentimentIntensityAnalyzer()

Genius_api_key = 'X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
headers = {
    'Authorization': 'Bearer X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
}
response = requests.get('https://api.genius.com/songs/378195', headers=headers)


# Original Code

data = response.json()
print(data)
title = data['response']['song']['title']
print(title)




# Using HTML should look like this 

soup = BeautifulSoup(response.text, "html.parser")
lyrics_finder = soup.find("div", class_="lyrics")
lyrics = lyrics_finder.text.strip()


# The thing about sentiment analysis is that there is only positive, negative, and neutral. We could technically create our own genres by maybe saying that neutral lyrics are "chill"
# or maybe we can combine the bpm and the sentiment analysis to determine that. For example, songs with bpm over 100 are usually pretty upbeat, and slower songs under 100 bpm
# have a higher likelihood of being negative/ neutral






# Here is how we could use html parser

# import requests
# from bs4 import BeautifulSoup
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from pydub import AudioSegment

# # Step 1: Scrape lyrics from genius.com
# song_url = "https://genius.com/artist/song-title"
# response = requests.get(song_url)
# soup = BeautifulSoup(response.text, "html.parser")
# lyrics_element = soup.find("div", class_="lyrics")
# lyrics = lyrics_element.text.strip()

# # Step 2: Preprocess lyrics
# lyrics = ''.join(c for c in lyrics if c.isalpha() or c.isspace())
# lyrics = lyrics.lower()
# words = nltk.word_tokenize(lyrics)

# # Step 3: Perform sentiment analysis
# sia = SentimentIntensityAnalyzer()
# sentiment_scores = sia.polarity_scores(lyrics)

# # Step 4: Classify song as happy or sad
# if sentiment_scores["compound"] > 0.5:
#     playlist = "happy"
# else:
#     playlist = "sad"

# # Step 5: Add song to appropriate playlist
# song = AudioSegment.from_file("song.mp3", format="mp3")
# if playlist == "happy":
#     happy_playlist.append(song)
# else:
#     sad_playlist.append(song)

