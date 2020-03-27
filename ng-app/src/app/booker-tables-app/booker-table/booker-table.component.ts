import { Component, OnInit, Input } from '@angular/core';
import { BookerEntriesAPI } from '../../services/http';

@Component({
  selector: 'app-booker-table',
  templateUrl: './booker-table.component.html',
  styleUrls: ['./booker-table.component.css']
})
export class BookerEntrieComponent implements OnInit {
  @Input('entry') entry = Object

  totalSum = 0;
  newRow = {
    "entry": 0,
    "name": "",
    "amount": 0,
    "category": 0,
  };

  constructor(private api: BookerEntriesAPI) {
    console.log(this.entry)
  }

  ngOnInit() {}

  ngDoCheck(){
    this.calculateTotal();
  }

  calculateTotal() {
    this.totalSum = 0;
    for (let row of this.entry["rows"]) {
      this.totalSum += row.amount;
    }
  }

  addRow() {
    this.newRow["entry"] = this.entry["id"] // ToDo
    this.api.addRow(this.newRow).subscribe(
      data => {
        this.entry["rows"].push(Object.assign({}, data));
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

  updateRow(row) {
    console.log('Updated: ', row);
  }

  removeRow(index) {
    this.entry["rows"].splice(index, 1);
  }
}
