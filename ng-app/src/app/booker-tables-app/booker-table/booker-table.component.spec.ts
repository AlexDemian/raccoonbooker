import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookerTableComponent } from './booker-table.component';

describe('BookerTableComponent', () => {
  let component: BookerTableComponent;
  let fixture: ComponentFixture<BookerTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookerTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookerTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
