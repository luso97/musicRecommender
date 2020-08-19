import { StartPageComponent } from './components/start-page/start-page.component';
import { MusicGenresComponent } from './components/music-genres/music-genres.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {path: '',   redirectTo: '/start', pathMatch: 'full' },
  {path:'start', component:StartPageComponent },
  {path:'music', component: MusicGenresComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
