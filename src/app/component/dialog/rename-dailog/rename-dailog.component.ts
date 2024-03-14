import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInput, MatInputModule } from '@angular/material/input';
import {
  MatDialogModule,
  MatDialogRef,
  MatDialog,
} from '@angular/material/dialog';

@Component({
  selector: 'app-rename-dailog',
  standalone: true,
  imports: [
    MatDialogModule,
    MatButtonModule,
    MatIconModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
  ],
  template: `
    <h2 mat-dialog-title>Tab name</h2>
    <mat-dialog-content>
      <mat-form-field>
        <mat-label>Fill tab name</mat-label>
        <input
          matInput
          #tab_name_input
          type="text"
          placeholder="Tab name"
          cdkFocusInitial
          (keyup.enter)="get_tab_name_input(tab_name_input.value)"
          required
        />
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button mat-dialog-close color="warn">Cancel</button>
      <button
        mat-button
        mat-dialog-close
        color="primary"
        type="submit"
        (click)="get_tab_name_input(tab_name_input.value)"
      >
        Ok
      </button>
    </mat-dialog-actions>
  `,
  styles: `
  mat-dialog-actions{ 
    justify-content: end;
  }
  `,
})
export class RenameDailogComponent {
  input_name: string = '';
  tab_name_input: any;

  constructor() {}
  get_tab_name_input(name: string) {
    // this.input_name = name;
    // console.log(name);
  }
}
