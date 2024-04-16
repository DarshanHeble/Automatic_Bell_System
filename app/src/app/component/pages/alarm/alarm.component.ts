import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { MatMenuModule } from '@angular/material/menu';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { RenameDailogComponent } from '../../dialog/rename-dailog/rename-dailog.component';
import { MatRippleModule } from '@angular/material/core';
import { AddAlarmDailogComponent } from '../../dialog/add-alarm-dailog/add-alarm-dailog.component';
import { MatDivider } from '@angular/material/divider';
import { CreateNewTabComponent } from '../../dialog/create-new-tab/create-new-tab.component';
import { ConfirmationDeleteDailogComponent } from '../../dialog/confirmation-delete-dailog/confirmation-delete-dailog.component';

import { Stc } from '../../../Stc';
import { MatTooltipModule } from '@angular/material/tooltip';

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
    MatTooltipModule,
  ],
})
export class AlarmComponent {
  bell_data: Stc[];
  activeTabId: string;
  isEnabled: boolean = true;

  setActiveTab(tabId: string) {
    this.activeTabId = tabId;
  }
  click() {}

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
            music_file_name: 'Bell.mp3',
            days: [
              { day: 'S', active: false },
              { day: 'M', active: true },
              { day: 'T', active: true },
              { day: 'W', active: true },
              { day: 'T', active: true },
              { day: 'F', active: true },
              { day: 'S', active: true },
            ],
            switch_state: false,
          },
          {
            time: '2:21 am',
            label: 'hello',
            music_file_name: 'Bell.mp3',
            days: [
              { day: 'S', active: false },
              { day: 'M', active: true },
              { day: 'T', active: true },
              { day: 'W', active: true },
              { day: 'T', active: true },
              { day: 'F', active: true },
              { day: 'S', active: true },
            ],
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
            music_file_name: 'Bell.mp3',
            days: [
              { day: 'S', active: false },
              { day: 'M', active: true },
              { day: 'T', active: true },
              { day: 'W', active: true },
              { day: 'T', active: true },
              { day: 'F', active: true },
              { day: 'S', active: true },
            ],
            switch_state: true,
          },
        ],
      },
    ];
    this.activeTabId = this.bell_data[0].tab_id;
  }
  update_switch(data: any) {
    if (data.switch_state) {
      data.switch_state = false;
    } else {
      data.switch_state = true;
    }
  }
  add_new_tab(result: any) {
    this.bell_data.push({
      tab_name: result,
      tab_icon: 'alarm',
      tab_id: result,
      data: [],
    });
  }
  Add_new_alarm(result: any) {
    var index = this.bell_data.indexOf(result.item);
    console.log(result.hr);
    var times = `${result.hr}:${result.min} ${result.ampm}`;
    console.log(times, typeof times);
    this.bell_data[index].data.push({
      time: times,
      label: result.label,
      music_file_name: result.music,
      days: result.days,
      switch_state: true,
    });
    // console.log(this.bell_data[index]);
  }
  rename_tab(result: any) {
    console.log(result.item);
    var index = this.bell_data.indexOf(result.item);
    this.bell_data[index].tab_name = result.name;
  }
  delete_tab(result: any) {
    console.log(result.tab_name);
    var index = this.bell_data.indexOf(result);
    console.log(result);
    this.bell_data.splice(index, 1);
    // console.log(this.bell_data.splice(index, 1));
  }
  // dailog ============
  open_rename_dailog(dict: Stc) {
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
  open_confirmation_delete_dailog(dict: Stc) {
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
      if (result) {
        this.delete_tab(result);
      }
    });
  }
  open_alarm_dailog(heading: string, dist: Stc) {
    const alarmdailogref = this.dailog.open(AddAlarmDailogComponent, {
      data: {
        title: heading,
        item_data: dist,
      },
    });
    alarmdailogref.afterClosed().subscribe((result) => {
      if (result) {
        this.Add_new_alarm(result);
      }
    });
  }
}
