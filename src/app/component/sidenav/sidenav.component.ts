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
  template: `
    <mat-nav-list class="side">
      <a
        mat-list-item
        class="menu-item"
        *ngFor="let item of menuItems()"
        [routerLink]="item.route"
        routerLinkActive="selected-menu-item"
        #rla="routerLinkActive"
        [activated]="rla.isActive"
      >
        <mat-icon
          matListItemIcon
          [fontSet]="
            rla.isActive ? 'material-icons' : 'material-icons-outlined'
          "
          >{{ item.icon }}</mat-icon
        >
        <!-- <span matListItemTitle>{{ item.label }}</span> -->
      </a>
    </mat-nav-list>
  `,
  styles: [
    `
      .side {
        display: flex;
        flex-direction: column;
        :last-child {
          margin-top: auto;
        }
      }
      .menu-item {
        transition: 0.5s;
      }
      .selected-menu-item {
        :before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          width: 5px;
          height: 100%;
          border-radius: 1px;
          background: blue;
        }
        // not working
        background-color: rgba(0, 0, 0, 0.05) !important;
      }
    `,
  ],
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
