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
import { MatDivider } from '@angular/material/divider';

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
  templateUrl: './alarm.component.html',
  styleUrl: './alarm.component.scss',
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
    AddAlarmDailogComponent,
    MatDivider,
  ],
})
export class AlarmComponent {
  bell_data: stc[];
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
  add_new_tab(result: any) {
    console.log(result);
    this.bell_data.push({
      tab_name: result.name,
      tab_icon: 'alarm',
      tab_id: result.name,
      data: [],
    });
  }
  rename_tab(result: any) {
    console.log(result.item);
    var index = this.bell_data.indexOf(result.item);
    this.bell_data[index].tab_name = result.name;
  }

  delete_tab(result: any) {
    console.log(result.item);
    var index = this.bell_data.indexOf(result.item);
    this.bell_data.splice(index, 1);
  }
  open_rename_dailog(heading: any, text: any, dict: any) {
    const namedailogref = this.dailog.open(RenameDailogComponent, {
      data: {
        title: heading,
        initial_text: text,
        item_data: dict,
      },
    });
    namedailogref.afterClosed().subscribe((result) => {
      if (result.heading == 'Rename this tab') {
        this.rename_tab(result);
      } else if (result.heading == 'Create new tab') {
        console.log('new');
        this.add_new_tab(result);
      } else if (result.heading == 'Delete this tab') {
        this.delete_tab(result);
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
