import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AnnFilterComponent } from '../../dialog/ann-filter/ann-filter.component';

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
    FormsModule,
    MatAutocompleteModule,
    MatTooltipModule,
  ],
})
export class AnnouncementComponent {
  textarea: string = '';
  update(input: any) {
    console.log(input);
  }
  open_ann_filter() {
    this.dailog.open(AnnFilterComponent, {});
  }
  constructor(private dailog: MatDialog) {}
}
