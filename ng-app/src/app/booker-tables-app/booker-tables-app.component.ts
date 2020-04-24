import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI, Entry, EntryRow } from '../services/http';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css']
})
export class BookerEntriesAppComponent implements OnInit {
  ngOnInit () {}
  
  entries: Entry [] = [];
  
  constructor(private api: BookerEntriesAPI) {
    this.api.getEntries().subscribe( data => { this.entries = data as Entry[] });
  }
}
