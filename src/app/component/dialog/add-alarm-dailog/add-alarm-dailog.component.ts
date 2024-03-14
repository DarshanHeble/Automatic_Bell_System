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
  template: `
    <h2 mat-dialog-title>{{ input_data.title }}</h2>
    <mat-dialog-content>
      <mat-form-field>
        <mat-icon matSuffix fontSet="material-icons-outlined">time </mat-icon>
        <!-- <input type="time" /> -->
      </mat-form-field>
      <mat-form-field>
        <mat-icon matPrefix fontSet="material-icons-outlined">label </mat-icon>
        <input matInput type="text" />
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-raised-button mat-dialog-close>
        <mat-icon>cancel</mat-icon>
        <span>close</span>
      </button>
      <button mat-raised-button mat-dialog-close>
        <mat-icon>save</mat-icon>
        <span>save</span>
      </button>
    </mat-dialog-actions>
  `,
  styles: ``,
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
