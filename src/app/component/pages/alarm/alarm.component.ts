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
import { CreateNewTabComponent } from '../../dialog/create-new-tab/create-new-tab.component';
import { ConfirmationDeleteDailogComponent } from '../../dialog/confirmation-delete-dailog/confirmation-delete-dailog.component';

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
  add_new_tab(result: string) {
    console.log(result);
    this.bell_data.push({
      tab_name: result,
      tab_icon: 'alarm',
      tab_id: result,
      data: [],
    });
  }
  rename_tab(result: any) {
    console.log(result.item);
    var index = this.bell_data.indexOf(result.item);
    this.bell_data[index].tab_name = result.name;
  }

  delete_tab(result: any) {
    console.log(result.tab_name);
    var index = this.bell_data.indexOf(result.item);
    this.bell_data.splice(index, 1);
  }
  open_rename_dailog(dict: stc) {
    const rename_dailogref = this.dailog.open(RenameDailogComponent, {
      data: {
        title: 'Rename this tab',
        initial_text: dict.tab_name,
        item_data: dict,
      },
    });
    rename_dailogref.afterClosed().subscribe((result) => {
      if (result) {
        this.rename_tab(result);
      }
    });
  }
  open_create_new_tab_dailog() {
    const rename_dailogref = this.dailog.open(CreateNewTabComponent, {
      width: '24rem',
      data: {
        title: 'Name this new tab',
        initial_text: '',
        // item_data: dict,
      },
    });
    rename_dailogref.afterClosed().subscribe((result) => {
      console.log(result);
      if (result) {
        this.add_new_tab(result);
      }
    });
  }
  open_confirmation_delete_dailog(dict: stc) {
    const delete_dailogref = this.dailog.open(
      ConfirmationDeleteDailogComponent,
      {
        data: {
          title: 'Name this new tab',
          tab_name: dict.tab_name,
          item_data: dict,
        },
      }
    );
    delete_dailogref.afterClosed().subscribe((result) => {
      console.log(result);
      if (result) {
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
