from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render, HttpResponseRedirect
import spotipy
from spotipy import oauth2
import bottle
from bottle import run
from spotipy import util
import requests
import time
import pandas as pd;
import os
from django.conf import settings


from spotipy.oauth2 import SpotifyOAuth
# Create your views here.
@api_view(['POST', 'GET'])
def login(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    SPOTIPY_CLIENT_ID = 'client_id';
    SPOTIPY_CLIENT_SECRET = 'client_secret';
    SCOPE = 'user-read-private user-read-email';
    CACHE = '.spotipyoauthcache'
    SPOTIPY_REDIRECT_URI = 'http://localhost:4200/start';
    print(request.__dict__)
    if request.method == 'GET':
        sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE, cache_path=".cache-")
        token_info = sp_oauth.get_cached_token()
        url = sp_oauth.get_auth_response()
        code = sp_oauth.parse_response_code(url)
        if code:
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
        sp = spotipy.Spotify(access_token)
        print("playlist")

    return JsonResponse(sp.current_user_playlists(), safe=False)
@api_view(['POST', 'GET'])
def getPlaylist(request):
    id = request.GET.get('id', None)
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    SPOTIPY_CLIENT_ID = 'client_id';
    SPOTIPY_CLIENT_SECRET = 'client_secret';
    SCOPE = 'user-read-private user-read-email';
    CACHE = '.spotipyoauthcache'
    SPOTIPY_REDIRECT_URI = 'http://localhost:4200/start';
    print(request.__dict__)
    if request.method == 'GET':
        sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI,
                                       scope=SCOPE, cache_path=".cache-")
        token_info = sp_oauth.get_cached_token()
        url = sp_oauth.get_auth_response()
        code = sp_oauth.parse_response_code(url)
        if code:
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
        sp = spotipy.Spotify(access_token)
        print("playlist")
        tracks=[];
        total=1000000;
        playlist=sp.playlist_tracks(id)
        sigue=True;
        tracks.extend(playlist['items']);
        tags=[];
        while playlist['next']:
            print(playlist['next'])
            playlist = sp.next(playlist)
            tracks.extend(playlist['items'])
        for t in tracks:
            headers = {
                'user-agent': 'musicRecommender'

            }
            name=t["track"]["name"].replace(" ","+")
            artname = t["track"]["artists"][0]["name"].replace(" ","+")
            print(name + "," + artname)
            r = requests.get(
                'http://ws.audioscrobbler.com/2.0/?method=track.search&track='+name+'&artist='+artname+'&limit=1&api_key=api_key&format=json',
                headers=headers)

            try:
                value = r.json()
                track = value['results']['trackmatches']['track'][0]
            except:
                track=None
                pass;
            print(track);
            if track:
                name=track['name'].replace(' ','+')
                artname=track['artist'].replace(' ','+')
                print(name+","+artname)
                print('iyo');
                r = requests.get(
                    'http://ws.audioscrobbler.com/2.0/?method=track.getTopTags&api_key=api_key&track='
                    +name+'&artist='+artname+ '&format=json',
                    headers)
                res = {};
                res['tags'] = []
                print(r.json())
                try:
                    for tag in r.json()['toptags']['tag']:
                        res['tags'].append(tag['name'].lower());
                    tags.extend(res['tags']);
                except:
                    print("no tags found ")
                    pass;
                print(len(tags))

        dfGenres = pd.read_csv(os.path.join(settings.BASE_DIR, 'rym/genresmap.csv'));
        print(tags);
        dfTags = pd.DataFrame(tags);
        print(dfTags);
        dfcount = pd.DataFrame(dfTags[0].value_counts())
        print(dfcount.head())
        dfGenres.set_index('Unnamed: 0',inplace=True)
        print(dfcount.head())

        print(dfGenres.head())
        print(dfcount.loc['flamenco'])
        dfFinal = dfcount.merge(dfGenres, how='inner', left_index=True, right_index=True)
        print(dfFinal.to_dict(orient="records"));
    return JsonResponse(dfFinal.to_dict(orient="records"), safe=False);