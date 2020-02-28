import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css']
})
export class BookerTablesAppComponent implements OnInit {

  constructor() { }

  ngOnInit() {}
  table_columns = [
    { "label": "Name", "property":"name", "type": "text" },
    { "label": "Amount", "property":"value", "type": "number" },
  ];

  tables = [
    [
      { "name": "Car", "value": 100500 },
      { "name": "Vacation", "value": 200 },
    ],
    [
      { "name": "Food", "value": 100 },
      { "name": "Utilities", "value": 20 },
    ],
  ]

  addTable () {
    this.tables.push([]);
  }

}
