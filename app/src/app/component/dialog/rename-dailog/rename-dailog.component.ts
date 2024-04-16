import { Component, Inject, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {
  MatDialogModule,
  MatDialogRef,
  MAT_DIALOG_DATA,
} from '@angular/material/dialog';

@Component({
  selector: 'app-rename-dailog',
  standalone: true,
  imports: [
    MatDialogModule,
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
  ],
  templateUrl: './rename-dailog.component.html',
  styleUrl: './rename-dailog.component.scss',
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
  onconfirm(name: string, heading: any, item: any): void {
    this.ref.close({ name, heading, item });
  }
}
