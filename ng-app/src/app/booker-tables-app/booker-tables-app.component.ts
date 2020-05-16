import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI, Entry } from '../services/http';
import {trigger,state,style,animate,transition} from '@angular/animations';

@Component({
  selector: 'app-booker-tables-app',
  templateUrl: './booker-tables-app.component.html',
  styleUrls: ['./booker-tables-app.component.css'],
  animations: [
    trigger('showHideSidebar', [
      state('show', style({
        width: '250px'
      })),
      state('collapse', style({
        width: '100px',
      })),
      transition('show => collapse', [
        animate('0.2s')
      ]),
      transition('collapse => show', [
        animate('0.1s')
      ]),
    ]),

    trigger('sideBarNotCollapsed', [
      state('no', style({
        width: '90%'
      })),
      state('yes', style({
        width: '80%',
      })),
      transition('yes => no', [
        animate('0.2s')
      ]),
      transition('no => yes', [
        animate('0.1s')
      ]),
    ]),
  ],
})
export class BookerEntriesAppComponent implements OnInit {
  ngOnInit () {}
  
  entries: Entry [] = [];
  
  constructor(private api: BookerEntriesAPI) {
    this.api.getEntries().subscribe( data => { this.entries = data as Entry[] });
  }

  settings = {
    showDiagrams: true,
    showCalculator: true, 
    showCalendar: true,
    showSidebar: true,
  }

  changeSettings(property, value) { 
    this.settings[property] = value;
    // TODO : push put to server
  }

}
