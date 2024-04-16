import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RenameDailogComponent } from './rename-dailog.component';

describe('RenameDailogComponent', () => {
  let component: RenameDailogComponent;
  let fixture: ComponentFixture<RenameDailogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RenameDailogComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RenameDailogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
