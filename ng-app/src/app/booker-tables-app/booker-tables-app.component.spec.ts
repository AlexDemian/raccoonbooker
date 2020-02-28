import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookerTablesAppComponent } from './booker-tables-app.component';

describe('BookerTablesAppComponent', () => {
  let component: BookerTablesAppComponent;
  let fixture: ComponentFixture<BookerTablesAppComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookerTablesAppComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookerTablesAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
