import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI } from '../services/http';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css']
})
export class BookerTablesAppComponent implements OnInit {

  tables = [];
  constructor(private api: BookerEntriesAPI) { }

  ngOnInit() {
    this.tables.concat(this.api.getTables());
  }

  // ToDo
  //addTable () {
  //  this.tables.push({});
  //}

  table_columns = [
    { "label": "Name", "property":"name", "type": "text" },
    { "label": "Amount", "property":"amount", "type": "number" },
  ];

}
