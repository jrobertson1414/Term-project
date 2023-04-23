import requests
Genius_api_key = 'X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
headers = {
    'Authorization': 'Bearer X5pP_hoFlaaLtLhQPeTOK6vq7nETrfo1JzQ9B4DLZVIMpY0Lw8Nup28dQwiDTEmY'
}
response = requests.get('https://api.genius.com/songs/378195', headers=headers)
data = response.json()
print(data)
title = data['response']['song']['title']
print(title)