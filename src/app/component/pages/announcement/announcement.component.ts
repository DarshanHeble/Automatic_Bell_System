import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule } from '@angular/material/menu';
@Component({
  selector: 'app-announcement',
  standalone: true,
  templateUrl: './announcement.component.html',
  styleUrl: './announcement.component.scss',
  imports: [
    MatIconModule,
    MatButtonModule,
    MatFormFieldModule,
    MatDialogModule,
    MatInputModule,
    MatMenuModule,
  ],
})
export class AnnouncementComponent {}
