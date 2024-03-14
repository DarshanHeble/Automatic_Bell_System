import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddAlarmDailogComponent } from './add-alarm-dailog.component';

describe('AddAlarmDailogComponent', () => {
  let component: AddAlarmDailogComponent;
  let fixture: ComponentFixture<AddAlarmDailogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddAlarmDailogComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddAlarmDailogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
