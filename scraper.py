#GET SONGS FROM SONG NAME + ARTIST
def artist_song(artist, song):
    base_url = 'https://genius.com/'
    link = artist + '-' + song + '-' + 'lyrics'     
    for i in link:
        if i is ' ':
            link = link.replace(i, '-')
    return base_url + link

#GET SONG NAME/LYRICS FROM GENIUS.COM
def get_lyrics(soup):
    song_json = {}
    for title in soup.find_all('h1', {'class' : 'header_with_cover_art-primary_info-title'}):
        song_name = title.text.strip()
    
    for div in soup.find_all('div', attrs = {'class': 'lyrics'}):
        song_json[song_name]= div.text.strip().split("\n")
    
    return song_json

#create function to retrieve access token
def get_cm_api_token(REFRESH_TOKEN):
    import requests
    import json
    response = requests.post(url='https://api.chartmetric.com/api/token', data={'refreshtoken' : REFRESH_TOKEN}, 
                             json={'Content-Type' : 'application/json'})
    results = response.json()
    api_token = results['token']
    return api_token

#create a function to get genre IDs
def get_genre_id(genre, access_token):
    response = requests.get(url='https://api.chartmetric.com/api/genres?name={}'.format(genre),
                           headers={'Authorization' : 'Bearer {}'.format(access_token)})
    return response.json()['obj']