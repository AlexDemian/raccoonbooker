import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookerEntrieComponent } from './booker-table.component';

describe('BookerEntrieComponent', () => {
  let component: BookerEntrieComponent;
  let fixture: ComponentFixture<BookerEntrieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookerEntrieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookerEntrieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
