import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-alarm',
  standalone: true,
  imports: [MatIconModule, MatButtonModule, MatIconModule, CommonModule],
  template: `
    <section class="alarm">
      <div class="alarm_sidebar">
        <!-- Add new tab button -->
        <button class="new_tab_btn" mat-raised-button extended>
          <mat-icon>add</mat-icon>
          <span> New tab </span>
        </button>

        <!-- All Tabs -->
        <div class="All_Tabs">
          <button
            class="tab"
            mat-raised-button
            extended
            *ngFor="let item of buttonLabels"
          >
            <mat-icon>chat</mat-icon>
            <span> {{ item }} </span>
          </button>
        </div>
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
        // display: flex;
        // flex-direction: column;
        height: 100vh;
        width: 16rem;
        padding: 1rem;
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
      .All_Tabs {
        margin-block-start: 2rem;

        .tab {
          width: 100%;
          margin-block-end: 0.3rem;
          justify-content: start;
        }
      }
    `,
  ],
})
export class AlarmComponent {
  buttonLabels = ['Action', 'Another Action', 'Third Action'];
}
