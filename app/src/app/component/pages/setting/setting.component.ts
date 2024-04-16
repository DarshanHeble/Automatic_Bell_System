import { Component } from '@angular/core';
import { MatIconModule } from '@angular/material/icon';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatRadioChange, MatRadioModule } from '@angular/material/radio';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-setting',
  standalone: true,
  imports: [MatIconModule, MatButtonModule, MatExpansionModule, MatRadioModule],
  templateUrl: './setting.component.html',
  styleUrl: './setting.component.scss',
})
export class SettingComponent {
  // async change_theme() {
  //   await window.darkMode.sytem();
  // }
  declare electronAPI: {
    sendMessageToMain: (channel: string, data: any) => void;
  };

  // Example usage
  changeTheme(event: MatRadioChange) {
    console.log(event);
    this.electronAPI.sendMessageToMain('changeTheme', { theme: 'dark' }); // Example data
  }
}
