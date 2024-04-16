import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { RouterLink, RouterModule, RouterOutlet } from '@angular/router';
import { MatListModule } from '@angular/material/list';

export type MenuItem = {
  icon: string;
  label: string;
  route: string;
};

@Component({
  selector: 'app-sidenav',
  standalone: true,
  imports: [
    CommonModule,
    MatIconModule,
    MatButtonModule,
    MatSidenavModule,
    RouterModule,
    MatListModule,
  ],
  templateUrl: './sidenav.component.html',
  styleUrl: './sidenav.component.scss',
})
export class SidenavComponent {
  menuItems = signal<MenuItem[]>([
    {
      icon: 'notifications',
      label: 'Alarm',
      route: 'alarm',
    },
    {
      // icon: 'campaign',
      icon: 'volume_up',
      label: 'Announcement',
      route: 'announcement',
    },
    {
      icon: 'settings',
      label: 'Settings',
      route: 'settings',
    },
  ]);
}
