import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SpotifyService {

  constructor(private http:HttpClient) { }
  baseUrl = 'http://localhost:7000/api/'
  my_client_id = '282b72bd767a4e16b32b020f497cc899';
  client_secret = '00721ec0e74d4acfa3cc7ae0b714973e';
  scopes = 'user-read-private user-read-email';
  redirect_uri = 'localhost:4600/start';

  connectSpotify(){
    return this.http.get(this.baseUrl+'spotify/login');
  }
  sendPlaylist(data){
    return this.http.get(this.baseUrl+'spotify/playlist?id='+data);
  }
}
