import { SpotifyService } from './../../services/spotify.service';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormBuilder, FormGroup,Validators, FormControl, FormArray, Form } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.css']
})
export class StartPageComponent implements OnInit {

  constructor(
    private spotifyService: SpotifyService,
    private formBuilder: FormBuilder,
    private router: Router) { }
  playlists=[];
  formSpotify:FormGroup;

  ngOnInit(): void {
    this.formSpotify=this.formBuilder.group({
      playlist:['']
    })

  }
  connectSpotify(){
    this.spotifyService.connectSpotify().subscribe(response=>{
      this.playlists=response['items'];
    });
  }

  submit(){
    this.spotifyService.sendPlaylist(this.formSpotify.get('playlist').value).subscribe(response=>{
      console.log(response);
      this.router.navigate(["music",{'genres':JSON.stringify(response)}]);
    });
  }

}
