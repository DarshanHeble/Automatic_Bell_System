import { Day } from './Day';

export interface Bell {
  time: string;
  label: string;
  music_file_name: string;
  days: Day[];
  switch_state: boolean;
}
