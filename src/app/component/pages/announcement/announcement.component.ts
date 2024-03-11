import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-announcement',
  standalone: true,
  imports: [MatIconModule, MatButtonModule],
  template: ` <section><h1>Announcement</h1></section> `,
  styles: `
  section{
    padding: 1rem 3rem;
    height: -webkit-fill-available;
  }
  h1{
    font-size: 2.4em;
  }
  `,
})
export class AnnouncementComponent {}
