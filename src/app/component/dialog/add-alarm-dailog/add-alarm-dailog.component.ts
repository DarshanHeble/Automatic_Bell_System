import { Component, Inject, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import {
  MAT_DIALOG_DATA,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-add-alarm-dailog',
  standalone: true,
  imports: [
    MatDialogModule,
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
  ],
  templateUrl: './add-alarm-dailog.component.html',
  styleUrl: './add-alarm-dailog.component.scss',
})
export class AddAlarmDailogComponent implements OnInit {
  input_data: any;
  constructor(
    private ref: MatDialogRef<AddAlarmDailogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: object
  ) {}

  ngOnInit(): void {
    this.input_data = this.data;
    // throw new Error('Method not implemented.');
  }
}
