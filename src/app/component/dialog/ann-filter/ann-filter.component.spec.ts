import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnnFilterComponent } from './ann-filter.component';

describe('AnnFilterComponent', () => {
  let component: AnnFilterComponent;
  let fixture: ComponentFixture<AnnFilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AnnFilterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AnnFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
