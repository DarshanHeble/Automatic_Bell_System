import { Component, Inject, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import {
  MAT_DIALOG_DATA,
  MatDialogRef,
  MatDialogModule,
} from '@angular/material/dialog';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-confirmation-delete-dailog',
  standalone: true,
  imports: [MatDialogModule, MatIconModule, MatButtonModule],
  templateUrl: './confirmation-delete-dailog.component.html',
  styleUrl: './confirmation-delete-dailog.component.scss',
})
export class ConfirmationDeleteDailogComponent implements OnInit {
  input_data: any;
  constructor(
    private ref: MatDialogRef<ConfirmationDeleteDailogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {}

  ngOnInit(): void {
    this.input_data = this.data;
  }
  onconfirm(item: any): void {
    this.ref.close(item);
  }
}
