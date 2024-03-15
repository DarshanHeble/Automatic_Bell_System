import { CommonModule } from '@angular/common';
import { Component, Inject, OnInit, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { MatMenuModule } from '@angular/material/menu';
import {
  MAT_DIALOG_DATA,
  MatDialog,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { RenameDailogComponent } from '../../dialog/rename-dailog/rename-dailog.component';
import { MatRippleModule } from '@angular/material/core';
import { AddAlarmDailogComponent } from '../../dialog/add-alarm-dailog/add-alarm-dailog.component';

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
    MatMenuModule,
    MatRippleModule,
  ],
  templateUrl: './alarm.component.html',
  styleUrl: './alarm.component.scss',
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
    const namedailogref = this.dailog.open(RenameDailogComponent, {
      data: {
        title: heading,
        initial_text: text,
      },
    });
    namedailogref.afterClosed().subscribe((result) => {
      if (result.heading == 'Rename the tab') {
        this.rename(result);
      } else if (result.heading == 'Create new tab') {
        this.add_new_tab(result);
      }
    });
  }
  open_alarm_dailog(heading: string) {
    const alarmdailogref = this.dailog.open(AddAlarmDailogComponent, {
      data: {
        title: heading,
      },
    });
  }
}
