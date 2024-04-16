import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateNewTabComponent } from './create-new-tab.component';

describe('CreateNewTabComponent', () => {
  let component: CreateNewTabComponent;
  let fixture: ComponentFixture<CreateNewTabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateNewTabComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CreateNewTabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
