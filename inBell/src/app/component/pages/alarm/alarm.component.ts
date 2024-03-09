import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';

import { structure } from '../../../structuer';
import { Bell } from '../../../Bell';

interface stc {
  tab_name: string;
  tab_icon: string;
  tab_id: string;
  data: Bell[];
}

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
            *ngFor="let item of data1"
            (click)="setActiveTab(item.tab_id)"
          >
            <mat-icon> {{ item.tab_icon }} </mat-icon>
            <span> {{ item.tab_name }} </span>
          </button>
        </div>
      </div>
      <div class="alarm_window">
        <div
          class="window"
          *ngFor="let item of data1"
          id="{{ item.tab_id }}"
          [ngClass]="{ active: item.tab_id === activeTabId }"
        >
          <mat-card *ngFor="let data of item.data">
            <mat-card-header>
              <mat-card-subtitle> {{ data.label }} </mat-card-subtitle>
              <mat-card-title> {{ data.time }} </mat-card-title>
            </mat-card-header>
            <mat-card-content> {{ data.days }}</mat-card-content>
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
        overflow-y: auto;
      }
      .alarm_window {
        overflow: hidden;
        height: 100vh;
        width: 100%;
        background: pink;
        position: relative;

        .window {
          position: absolute;

          width: -webkit-fill-available;
          height: -webkit-fill-available;
          padding: 3rem;
          display: grid;
          grid-template-columns: repeat(
            auto-fit,
            minmax(min(14rem, 100%), 1fr)
          );
          grid-template-rows: repeat(auto-fit, 10rem);
          gap: 1rem;
          z-index: 10;
          background-color: pink;

          mat-card {
            min-width: 14rem;
            height: 10rem;
          }
        }
        .window.active {
          // background-color: red;
          z-index: 11;
          animation: ActiveTab 1s ease-in-out;
        }
      }

      @keyframes ActiveTab {
        0% {
          transform: translateX(100%);
        }
        100% {
          transform: translateX(0%);
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
  bell_chats = ['Classes', 'Examamination'];
  data: Bell[][];
  data1: stc[];
  activeTabId: string = '';

  setActiveTab(tabId: string) {
    this.activeTabId = tabId;
  }

  constructor() {
    // this.data = [
    //   {
    //     Class: [
    //       {
    //         time: '2:21am',
    //         label: 'hello1',
    //         days: ['monday', 'tuesday'],
    //         switch_state: true,
    //       },
    //     ],
    //     Class: [
    //       {
    //         time: '2:21am',
    //         label: 'hello1',
    //         days: ['monday', 'tuesday'],
    //         switch_state: true,
    //       },
    //     ],
    //   },
    // ];
    this.data = [
      [
        {
          time: '2:21am',
          label: 'hello1',
          days: ['monday', 'tuesday'],
          switch_state: true,
        },
        {
          time: '2:21am',
          label: 'hello1',
          days: ['monday', 'tuesday'],
          switch_state: true,
        },
      ],
      [
        {
          time: '2:21am',
          label: 'hello1',
          days: ['monday', 'tuesday'],
          switch_state: true,
        },
      ],
    ];
    this.data1 = [
      {
        tab_name: 'Classes',
        tab_icon: 'alarm',
        tab_id: 'Classes',
        data: [
          {
            time: '2:21am',
            label: 'hello',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
          {
            time: '2:21am',
            label: 'hello',
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
        tab_name: 'exam',
        tab_icon: 'campaign',
        tab_id: 'exam',
        data: [
          {
            time: '2:21am',
            label: 'hello1',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
          {
            time: '2:21am',
            label: 'hello1',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
        ],
      },
    ];
  }
  AddActive(id: string) {
    console.log('#' + id);
  }
}
