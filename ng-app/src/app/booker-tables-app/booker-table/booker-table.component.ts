import { Component, OnInit, Input } from '@angular/core';
import { BookerEntriesAPI, Entry, EntryRow } from '../../services/http';


@Component({
  selector: 'app-booker-table',
  templateUrl: './booker-table.component.html',
  styleUrls: ['./booker-table.component.css']
})
export class BookerEntrieComponent implements OnInit {
  @Input('entry') entry = Entry

  calculations = {
    incomesSum: 0,
    outcomesSum: 0,
    totalSum: 0,
  }  

  newRow = {
    "entry": 0,
    "name": "",
    "amount": 0,
    "category": 0,
  };

  filters = {
    deleted: false
  };

  constructor(private api: BookerEntriesAPI) {
    this.entry['rows'] = this.entry['rows'] as EntryRow[];  
  }

  ngOnInit() {}

  ngDoCheck(){
    this.calculateTotal();
  }

  calculateTotal() {
    
    this.calculations = {
      incomesSum: 0,
      outcomesSum: 0,
      totalSum: 0,
    }  

    for (let row of this.entry['rows']) {
      let value = Number(row.amount); // Todo
      this.calculations.totalSum += value;
      if (value > 0) {
        this.calculations.incomesSum += value
      } else {
        this.calculations.outcomesSum += value
      }
    }
  }

  addRow() {
    this.newRow["entry"] = this.entry["id"] // ToDo
    this.api.addRow(this.newRow).subscribe(
      data => {
        this.entry["rows"].push(data as EntryRow);
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
  }

  updateRow(row) {
    console.log('Updated: ', row);
    this.api.updateRow(row).subscribe(
      data => {
        row = data as EntryRow;
      },
    )
  }

  removeRestoreRow(row) {
    row.deleted = !row.deleted;
    this.updateRow(row);
  }

}
