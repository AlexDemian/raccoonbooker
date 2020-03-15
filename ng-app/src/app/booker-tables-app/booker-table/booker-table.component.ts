import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-booker-table',
  templateUrl: './booker-table.component.html',
  styleUrls: ['./booker-table.component.css']
})
export class BookerTableComponent implements OnInit {

  @Input('columns') columns = []
  @Input('rows') rows = []

  totalSum = 0;
  newRow = { "name": "", "value": 0 };

  constructor() {
  }

  ngOnInit() {}

  ngDoCheck(){
    this.calculateTotal();
  }

  calculateTotal() {
    this.totalSum = 0;
    for (let row of this.rows) {
      this.totalSum += row.value;
    }
  }

  addRow() {
    this.newRow.name = this.newRow.name || 'undefined';
    this.rows.push(Object.assign({}, this.newRow));
  }

  updateRow(row) {
    console.log('Updated: ', row);
  }

  removeRow(index) {
    this.rows.splice(index, 1);
  }
}
