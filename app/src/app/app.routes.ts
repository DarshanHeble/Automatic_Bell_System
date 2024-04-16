import { Routes } from '@angular/router';
import { AlarmComponent } from './component/pages/alarm/alarm.component';
import { AnnouncementComponent } from './component/pages/announcement/announcement.component';
import { SettingComponent } from './component/pages/setting/setting.component';

export const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'alarm',
  },
  {
    path: '',
    component: AlarmComponent,
  },
  {
    path: 'announcement',
    component: AnnouncementComponent,
  },
  {
    path: 'settings',
    component: SettingComponent,
  },
];
