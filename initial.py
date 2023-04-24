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








