import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI } from '../services/http';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css']
})
export class BookerTablesAppComponent implements OnInit {
  ngOnInit () {}
  tables = [];
  table_columns = [
    { "label": "Name", "property":"name", "type": "text" },
    { "label": "Desctipion", "property": "desctipion", "type": "text" },
    { "label": "Category", "property": "category_name", "type": "text" },
    { "label": "Amount", "property":"amount", "type": "number" },
  ];

  constructor(private api: BookerEntriesAPI) {
    this.getEntries();
  }

  getEntries = () => {
    this.api.getTables().subscribe(
      data => {
        this.tables = data;
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

}
