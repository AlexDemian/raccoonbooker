import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  expression = ""
  total = '= ...';

  calculate() {
    try {
      this.total = "= " + eval(this.expression);
    } 
    catch {
      this.total = '= ...';
    }
  }

}
