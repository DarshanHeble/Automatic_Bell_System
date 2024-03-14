import {
  Component,
  ViewChild,
  ElementRef,
  AfterViewInit,
  Input,
  Output,
  EventEmitter,
  Inject,
  OnInit,
} from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInput, MatInputModule } from '@angular/material/input';
import {
  MatDialogModule,
  MatDialogRef,
  MatDialog,
  MAT_DIALOG_DATA,
} from '@angular/material/dialog';
import { DialogRef } from '@angular/cdk/dialog';

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
    <h2 mat-dialog-title>{{ input_data.title }}</h2>
    <mat-dialog-content>
      <mat-form-field>
        <mat-label>Fill tab name</mat-label>
        <input
          matInput
          #tab_name_input
          type="text"
          placeholder="Tab name"
          cdkFocusInitial
          value="{{ input_data.initial_text }}"
          (keyup.enter)="get_tab_name_input(tab_name_input.value)"
          required
        />
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button mat-dialog-close color="warn">Cancel</button>
      <button
        mat-button
        mat-dialog-close=""
        color="primary"
        type="submit"
        (click)="onconfirm(tab_name_input.value)"
      >
        <!-- (click)="get_tab_name_input(tab_name_input.value)" -->
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
export class RenameDailogComponent implements OnInit {
  input_name: string = '';
  // tab_name_input: string = '';
  input_data: any;

  constructor(
    private ref: MatDialogRef<RenameDailogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  ngOnInit(): void {
    // throw new Error('Method not implemented.');
    this.input_data = this.data;
  }

  get_tab_name_input(name: string) {
    // this.input_name = name;
    // console.log(name);
  }
  onconfirm(name: string): void {
    this.input_name = name;
    console.log(name + 'by dailog');

    let d = 'hello';
    this.ref.close();
  }
}
