import { CookieService } from "angular2-cookie/core";
import { Injectable } from '@angular/core';
import { DatePipe } from '@angular/common';

@Injectable()
export class CookedSettingsManager {
    constructor(private cookies: CookieService, private datePipe: DatePipe){}

    cookiesSettingsKey = 'interfaceSettings'
    cookiesFiltersKey = 'filters'
    backendDateFormat = 'mm/dd/yyyy'

    defaultApiFilters = {
        dateTo: null,
        dateFrom: null,
        sheet: null,
        name: ''
    }

    defaultSettings = {
        showDiagrams: true,
        showCalculator: true, 
        showCalendar: true,
        showSidebar: true,
        entriesFilterOrAddMode: true,
    }

    getSettings () {
        return (this.cookies.getObject(this.cookiesSettingsKey) || this.defaultSettings)
    }
    
    getApiFilters () {
        return (this.cookies.getObject(this.cookiesFiltersKey) || this.defaultApiFilters)
    }

    saveSettingsAndFiltersAtCookies (settingsObject: Object, apiFiltersObject: Object) {
        this.cookies.putObject(this.cookiesSettingsKey, settingsObject)
        this.cookies.putObject(this.cookiesFiltersKey, apiFiltersObject)
    }
}

export const datePickerSettings = {
    dateFormat: 'mmm d, yyyy', //Adapt API first
    selectorWidth: '220px'
};