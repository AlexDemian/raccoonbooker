import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI } from '../services/http';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css']
})
export class BookerEntriesAppComponent implements OnInit {
  ngOnInit () {}
  entries = [];
  constructor(private api: BookerEntriesAPI) {
    this.getEntries();
  }

  getEntries = () => {
    this.api.getEntries().subscribe(
      data => {
        this.entries = data;
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
