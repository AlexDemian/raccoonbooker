import { Component, OnInit } from '@angular/core';
import { BookerEntriesAPI, Entry } from '../services/http';
import { CookedSettingsManager, datePickerSettings } from '../services/settingsManager';
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
        width: '50px',
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
        width: '95%'
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
  settings: Object = {};
  apiFilters: Object = {};
  datePickerOptions = datePickerSettings;

  constructor(
    private api: BookerEntriesAPI, 
    private settingsManager: CookedSettingsManager,
  ) {
    this.apiFilters = this.settingsManager.getApiFilters()
    this.settings = this.settingsManager.getSettings()
    this.getEntries();
  }
  
  ngDoCheck() {
    this.settingsManager.saveSettingsAndFiltersAtCookies(this.settings, this.apiFilters);
  }

  getEntries() {
    this.api.getEntries(this.apiFilters).subscribe( data => { this.entries = data as Entry[] });
  }

  updateEntry() {}

  addEntry() {}

  deleteEntry() {}

}
