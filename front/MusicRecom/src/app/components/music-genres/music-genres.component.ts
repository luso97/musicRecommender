import { Component, OnInit, ElementRef } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-music-genres',
  templateUrl: './music-genres.component.html',
  styleUrls: ['./music-genres.component.css']
})
export class MusicGenresComponent implements OnInit {

  constructor(
    private router: Router,
    private actRoute: ActivatedRoute,
  ) { }
  vals :string="";

  ngOnInit(): void {
    console.log(this.actRoute.snapshot.params['genres'])
    this.vals = this.actRoute.snapshot.params['genres'];
    var inputs:any[] = JSON.parse(this.vals)
    var c = document.getElementById("canvasito") as HTMLCanvasElement
    console.log(c);
    var context = c.getContext("2d");

    var max = 254;
    for (var i=0;i<inputs.length;i++){
      var x=inputs[i];
      if(i==0){
        max = parseInt(x['0'])
      }
      context.beginPath()

      console.log(x)
      var f = 254*(parseInt(x['0'])/max)
      console.log(f)
      context.fillStyle = "rgba("+(254-f)+","+(254-f)+",48,0.3)";
      console.log(context)
      context.moveTo(x['y']+12, x['x']+2);
      context.arc(x['y']+12, x['x']+2, 50, 0, Math.PI * 2, true);
      context.fill();


    }


    context.beginPath();
    context.rect(20, 20, 1500,17000);
    context.stroke();
    console.log('tu')



  }

}
