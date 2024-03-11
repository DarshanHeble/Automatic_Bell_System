import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';

interface stc {
  tab_name: string;
  tab_icon: string;
  tab_id: string;
  data: Bell[];
}
interface Bell {
  time: string;
  label: string;
  days: string[];
  switch_state: boolean;
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
        <button
          class="new_tab_btn"
          mat-raised-button
          extended
          (click)="add_new_tab()"
        >
          <mat-icon>add</mat-icon>
          <span> New tab </span>
        </button>

        <!-- All Tabs -->
        <div class="All_Tabs">
          <div class="alarm_tab">
            <h3>All Tabs</h3>
            <button
              class="tab"
              mat-raised-button
              extended
              *ngFor="let item of bell_data"
              (click)="setActiveTab(item.tab_id)"
              (dblclick)="rename()"
              [ngClass]="{ active: item.tab_id === activeTabId }"
            >
              <mat-icon> {{ item.tab_icon }} </mat-icon>
              <span> {{ item.tab_name }} </span>
            </button>
          </div>
        </div>
      </div>
      <div class="alarm_window">
        <div
          class="window"
          *ngFor="let item of bell_data"
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
          <button mat-fab class="add">
            <mat-icon>add</mat-icon>
          </button>
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
          overflow-y: auto;

          mat-card {
            min-width: 14rem;
            height: 10rem;
          }
          .add {
            position: fixed;
            bottom: 4rem;
            right: 4rem;
          }
        }
        .window.active {
          // background-color: red;
          z-index: 11;
          animation: ActiveTab 0.5s ease-in-out;
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
        .tab.active {
          background-color: lightblue;
        }
      }
    `,
  ],
})
export class AlarmComponent {
  bell_data: stc[];
  activeTabId: string;

  setActiveTab(tabId: string) {
    this.activeTabId = tabId;
  }

  constructor() {
    this.bell_data = [
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
        tab_icon: 'alarm',
        tab_id: 'exam',
        data: [
          {
            time: '2:21am',
            label: 'hello1',
            days: ['monday', 'tuesday'],
            switch_state: true,
          },
        ],
      },
    ];
    this.activeTabId = this.bell_data[0].tab_id;
  }
  add_new_tab() {
    this.bell_data.push({
      tab_name: 'exam',
      tab_icon: 'alarm',
      tab_id: 'exam',
      data: [],
    });
  }
  rename() {
    console.log('rename');
  }
}