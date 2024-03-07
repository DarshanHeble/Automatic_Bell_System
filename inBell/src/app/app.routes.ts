import { Routes } from '@angular/router';
import { AlarmComponent } from './component/pages/alarm/alarm.component';
import { AnnouncementComponent } from './component/pages/announcement/announcement.component';
import { SettingsComponent } from './component/pages/settings/settings.component';

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'alarm',
  },
  {
    path: 'alarm',
    component: AlarmComponent,
  },
  {
    path: 'announcement',
    component: AnnouncementComponent,
  },
  {
    path: 'settings',
    component: SettingsComponent,
  },
];
