import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BookerEntriesAppComponent } from './booker-tables-app.component';

describe('BookerEntriesAppComponent', () => {
  let component: BookerEntriesAppComponent;
  let fixture: ComponentFixture<BookerEntriesAppComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BookerEntriesAppComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BookerEntriesAppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
