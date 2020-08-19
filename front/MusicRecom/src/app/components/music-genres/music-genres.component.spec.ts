import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MusicGenresComponent } from './music-genres.component';

describe('MusicGenresComponent', () => {
  let component: MusicGenresComponent;
  let fixture: ComponentFixture<MusicGenresComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MusicGenresComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MusicGenresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
