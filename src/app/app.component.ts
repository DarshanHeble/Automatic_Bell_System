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
    SidenavComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'angel';
}
