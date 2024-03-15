import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmationDeleteDailogComponent } from './confirmation-delete-dailog.component';

describe('ConfirmationDeleteDailogComponent', () => {
  let component: ConfirmationDeleteDailogComponent;
  let fixture: ComponentFixture<ConfirmationDeleteDailogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ConfirmationDeleteDailogComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ConfirmationDeleteDailogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
