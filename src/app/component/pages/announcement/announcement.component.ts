import { AsyncPipe, CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatChipsModule } from '@angular/material/chips';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';
import { MatAutocompleteModule } from '@angular/material/autocomplete';

import * as fs from 'fs';
import * as path from 'path';
import { Observable, map, startWith } from 'rxjs';

@Component({
  selector: 'app-announcement',
  standalone: true,
  templateUrl: './announcement.component.html',
  styleUrl: './announcement.component.scss',
  imports: [
    CommonModule,
    MatIconModule,
    MatButtonModule,
    MatFormFieldModule,
    MatDialogModule,
    MatInputModule,
    MatMenuModule,
    MatChipsModule,
    FormsModule,
    MatAutocompleteModule,
    ReactiveFormsModule,
    AsyncPipe,
  ],
})
export class AnnouncementComponent {
  hr_btn_text: number = 1;
  min_btn_text: number = 0;
  active_am_or_pm: string = 'am';
  // files: any = fs.readdirSync('../../../../assets/music');
  files: string[] = ['Bell.mp3', 'Break.mp3'];
  recent_file: string = this.files[0];
  label: string = 'Period';
  value = 'Clear me';

  mycontrol = new FormControl('');
  // filterd_files: Observable<string[]>;

  chips = [
    { day: 'S', active: false },
    { day: 'M', active: true },
    { day: 'T', active: true },
    { day: 'W', active: true },
    { day: 'T', active: true },
    { day: 'F', active: true },
    { day: 'S', active: true },
  ];
  on_hr_scroll(event: WheelEvent, btn: any): void {
    if (event.deltaY > 0) {
      // down wheel
      if (this.hr_btn_text == 12) {
        this.hr_btn_text = 1;
      }
      this.hr_btn_text++;
    } else if (event.deltaY < 0) {
      // Up wheel
      if (this.hr_btn_text == 1) {
        this.hr_btn_text = 12;
      }
      this.hr_btn_text--;
    }
  }
  on_min_scroll(event: WheelEvent, btn: any): void {
    if (event.deltaY > 0) {
      // down wheel
      if (this.min_btn_text == 59) {
        this.min_btn_text = 0;
      }
      this.min_btn_text++;
    } else if (event.deltaY < 0) {
      // Up wheel
      if (this.min_btn_text == 0) {
        this.min_btn_text = 59;
      }
      this.min_btn_text--;
    }
  }
  menu_hr_click(item: number) {
    this.hr_btn_text = item;
  }
  menu_min_click(item: number) {
    this.min_btn_text = item;
  }
  set_ampm_active(item: any) {
    if (item !== this.active_am_or_pm) {
      this.active_am_or_pm = item;
    }
  }
  toogle(item: any) {
    item.active = !item.active;
  }
  add_to_recent(item: string) {
    this.recent_file = item;
  }
  constructor() {}
}
