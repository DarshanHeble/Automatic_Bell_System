import { Component } from '@angular/core';
import { MatButtonModule, MatIconButton } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-alarm',
  standalone: true,
  imports: [MatIconModule, MatButtonModule],
  template: `
    <section class="alarm">
      <div class="alarm_sidebar">
        <button mat-raised-button extended>
          <mat-icon>add</mat-icon>
          <span> New tab </span>
        </button>
      </div>
      <div class="alarm_window"></div>
    </section>
  `,
  styles: [
    `
      .alarm {
        width: 100%;
        display: flex;
        // flex-direction: column;
      }
      .alarm_sidebar {
        height: 100vh;
        width: 16rem;
        background: yellow;
        // border: solid red;
      }
      .alarm_window {
        height: 100vh;
        width: 100%;
        background: pink;
        // border: solid blue;
      }
      button {
        border-radius: 5rem;
      }
    `,
  ],
})
export class AlarmComponent {}
