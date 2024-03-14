import { CommonModule } from '@angular/common';
import { Component, Inject, OnInit, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { RenameDailogComponent } from '../../dialog/rename-dailog/rename-dailog.component';

interface stc {
  tab_name: string;
  tab_icon: string;
  tab_id: string;
  data: Bell[];
}
interface Bell {
  time: string;
  label: string;
  music_file_name: string;
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
    MatDialogModule,
  ],
  template: `
    <section class="alarm">
      <div class="alarm_sidebar">
        <!-- Add new tab button -->
        <button
          class="new_tab_btn"
          mat-raised-button
          extended
          (click)="open_dailog('Create New Tab')"
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
              (dblclick)="open_dailog('Rename the tab', item.tab_name)"
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
              <div class="card-title" style="">
                <mat-card-title>
                  {{ data.time.split(' ')[0] }}
                </mat-card-title>
                <mat-card-subtitle>
                  {{ data.time.split(' ')[1] }}
                </mat-card-subtitle>
              </div>

              <mat-slide-toggle></mat-slide-toggle>
            </mat-card-header>
            <mat-card-content>
              <p class="label">{{ data.label }}</p>
              <p class="music">{{ data.music_file_name }}</p>
              <p class="days" *ngFor="let day of data.days">{{ day }} &nbsp;</p>
            </mat-card-content>
            <!-- <mat-card-actions> </mat-card-actions> -->
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

          .card-title {
            display: flex;
            align-items: baseline;

            mat-card-subtitle {
              font-size: x-large;
            }
          }
          mat-card-title {
            font-size: 3.5rem;
            color: #484848;
            line-height: 3rem;
            height: 3rem;
          }
          mat-slide-toggle {
            margin-left: auto;
          }

          mat-card {
            min-width: 14rem;
            height: 10rem;
          }
          mat-card-content {
            margin-top: auto;

            p {
              margin-block: 4px;
            }
            .label {
              font-size: large;
              font-weight: 500;
            }
            .days {
              display: inline;
            }
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
          animation: ActiveTab 0.3s ease-in-out;
        }
      }

      @keyframes ActiveTab {
        0% {
          opacity: 0.3;
          transform: translateX(50%);
        }
        100% {
          opacity: 1;
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
  input_name: string = '';

  activeTabId: string;

  setActiveTab(tabId: string) {
    this.activeTabId = tabId;
  }

  constructor(private dailog: MatDialog) {
    this.bell_data = [
      {
        tab_name: 'Classes',
        tab_icon: 'alarm',
        tab_id: 'Classes',
        data: [
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'],
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            days: ['mon', 'tue'],
            music_file_name: 'bell.mp3',
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
            switch_state: true,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
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
            time: '2:21 am',
            label: 'hello1',
            music_file_name: 'bell.mp3',
            days: ['mon', 'tue'],
            switch_state: true,
          },
        ],
      },
    ];
    this.activeTabId = this.bell_data[0].tab_id;
  }
  get_tab_name_input(name: string) {
    this.input_name = name;
    console.log(name);
  }
  add_new_tab(result: any) {
    this.bell_data.push({
      tab_name: result.name,
      tab_icon: 'alarm',
      tab_id: result.name,
      data: [],
    });
  }
  rename(result: any) {
    console.log(result);
  }
  open_dailog(heading: any, text: any = 'Tab') {
    const dailogref = this.dailog.open(RenameDailogComponent, {
      data: {
        title: heading,
        initial_text: text,
      },
    });
    dailogref.afterClosed().subscribe((result) => {
      if (result.heading == 'Rename the tab') {
        this.rename(result);
      } else if (result.heading == 'Create new tab') {
        this.add_new_tab(result);
      }
    });
  }
}
