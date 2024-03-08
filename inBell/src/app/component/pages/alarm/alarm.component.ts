import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { structure } from '../../../structuer';
import { Bell } from '../../../Bell';

@Component({
  selector: 'app-alarm',
  standalone: true,
  imports: [
    MatIconModule,
    MatButtonModule,
    MatIconModule,
    CommonModule,
    MatCardModule,
    MatSlideToggleModule,
    ScrollingModule,
  ],
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
          <h3>All Tabs</h3>
          <button
            class="tab"
            mat-raised-button
            extended
            *ngFor="let item of data"
          >
            <mat-icon>chat_bubble</mat-icon>
            <span> {{ item.tab_name }} </span>
          </button>
        </div>
      </div>
      <div class="alarm_window">
        <!-- <cdk-virtual-scroll-viewport class="window" itemSize=" {{ len }} ">
        </cdk-virtual-scroll-viewport> -->

        <div class="window">
          <mat-card *ngFor="let item of bell_data">
            <mat-card-header>
              <mat-card-subtitle> {{ item.time }} </mat-card-subtitle>
              <mat-card-title> {{ item.time }} </mat-card-title>
            </mat-card-header>
            <mat-card-content> {{ item.days }}</mat-card-content>
            <mat-card-actions>
              <button mat-icon-button>
                <mat-icon>edit</mat-icon>
              </button>
              <button mat-icon-button>
                <mat-icon>delete</mat-icon>
              </button>
              <mat-slide-toggle></mat-slide-toggle>
            </mat-card-actions>
          </mat-card>
        </div>
      </div>
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
        padding-inline: 1rem;
        background: yellow;
        overflow-y: scroll;
      }
      .alarm_window {
        overflow-y: hidden;
        height: 100vh;
        width: 100%;
        background: pink;

        .window {
          height: -webkit-fill-available;
          padding: 3rem;
          display: grid;
          grid-template-columns: repeat(
            auto-fit,
            minmax(min(14rem, 100%), 1fr)
          );
          grid-template-rows: repeat(auto-fit, 10rem);
          gap: 1rem;
          // overflow-y: auto;

          mat-card {
            min-width: 14rem;
            height: 10rem;
          }
        }
      }
      button {
        border-radius: 5rem;
      }
      .new_tab_btn {
        margin-block-start: 1rem;
      }
      .All_Tabs {
        margin-block-start: 2rem;
        h3 {
          margin: 0 0 0 4px;
        }

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
  data: structure[];
  len: number;
  bell_data: Bell;
  constructor() {
    this.data = [
      {
        tab_name: 'Classes',
        time: [
          {
            time: '2:21am',
            label: 'hello1',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
          {
            time: '2:21am',
            label: 'hello',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
        ],
      },
      {
        tab_name: 'exams',
        time: [
          {
            time: '2:21am',
            label: 'hello2',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
          {
            time: '2:21am',
            label: 'hello',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
        ],
      },
    ];
    this.len = this.data.length;

    for (let i = 0; i < this.data.length; i++) {
      for (let j = 0; j < i; j++) {
        // const element = i[j];
      }
      console.log(this.data[i].time);
    }
    for (let i of this.data[1].time) {
      this.bell_data = i;
      console.log(i);
    }
  }
}
