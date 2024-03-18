import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatChipsModule } from '@angular/material/chips';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';

import * as fs from 'fs';
import * as path from 'path';

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
  ],
})
export class AnnouncementComponent {
  hr_btn_text: number = 1;
  min_btn_text: number = 0;
  active_am_or_pm: string = 'am';
  files: any = fs.readdirSync('../../../../assets/music');

  chips = [
    { day: 'sun', active: false },
    { day: 'mon', active: false },
    { day: 'tue', active: false },
    { day: 'wed', active: false },
    { day: 'thu', active: false },
    { day: 'fri', active: false },
    { day: 'sat', active: false },
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
  constructor() {
    console.log(this.files);
  }
}
