import { Component, Inject, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import {
  MAT_DIALOG_DATA,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';

@Component({
  selector: 'app-create-new-tab',
  standalone: true,
  imports: [
    MatDialogModule,
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
  ],
  templateUrl: './create-new-tab.component.html',
  styleUrl: './create-new-tab.component.scss',
})
export class CreateNewTabComponent implements OnInit {
  input_data: any;
  constructor(
    private ref: MatDialogRef<CreateNewTabComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  ngOnInit(): void {
    this.input_data = this.data;
  }
  onconfirm(name: string): void {
    this.ref.close(name);
  }
}
