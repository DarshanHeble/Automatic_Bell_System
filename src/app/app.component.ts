import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

// material components
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatSidenavModule } from '@angular/material/sidenav';

// UI component
import { SidenavComponent } from './component/sidenav/sidenav.component';
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    // HttpClientModule,
    // material components
    MatButtonModule,
    MatIconModule,
    MatSidenavModule,
    // UI component
    SidenavComponent,
    // MainWindowComponent,
  ],
  template: `
    <!-- <router-outlet /> -->
    <mat-sidenav-container>
      <mat-sidenav opened mode="side" [style.width]="''">
        <!-- side nav component -->
        <app-sidenav></app-sidenav>
      </mat-sidenav>

      <mat-sidenav-content class="content">
        <!-- <router-outlet /> -->
        <router-outlet></router-outlet>
      </mat-sidenav-content>
    </mat-sidenav-container>
    <!-- <app-main-window></app-main-window> -->
  `,
  styles: [
    `
      * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
        cursor-pointer: none;
      }

      app-main-window {
        width: -webkit-fill-available;
      }
      mat-sidenav-container {
        height: 100vh;
      }
      mat-sidenav {
        width: 3.5rem;
        // padding-inline: 5px;
      }
      mat-sidenav-content {
        width: -webkit-fill-available;
        // width: 20rem;
      }
    `,
  ],
})
export class AppComponent {
  title = 'inBell';
  constructor() {
    // providers: [
    //   {
    //     provide: MAT_FORM_FIELD_DEFAULT_OPTIONS,
    //     useValue: { appearance: 'outline' },
    //   },
    // ];
  }
}
