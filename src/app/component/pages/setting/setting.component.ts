import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatRadioModule } from '@angular/material/radio';

@Component({
  selector: 'app-setting',
  standalone: true,
  imports: [MatIconModule, MatButtonModule, MatExpansionModule, MatRadioModule],
  template: `
    <section>
      <h1>Settings</h1>

      <mat-expansion-panel>
        <mat-expansion-panel-header>
          <mat-panel-title>
            <mat-icon fontSet="material-icons-outlined">palette</mat-icon>
            Select app theme
          </mat-panel-title>
        </mat-expansion-panel-header>
        <mat-radio-group aria-label="Select an option">
          <mat-radio-button value="Light">Light</mat-radio-button>
          <mat-radio-button value="Dark">Dark</mat-radio-button>
          <mat-radio-button value="System_theme">System theme</mat-radio-button>
        </mat-radio-group>
      </mat-expansion-panel>
    </section>
  `,
  styles: `
  section{
    padding: 1rem 3rem;
    height: -webkit-fill-available;
    // display: flex;
    // flex-direction: column;
    // justify-content: start;
    // align-items: center;
  }
  h1{
    font-size: 2.4em;
  }
  mat-expansion-panel{
    width: 40rem;

    mat-icon{
      margin-right : 2rem;
    }
    mat-radio-group{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
  }
  `,
})
export class SettingComponent {}
