// Angular
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DatePipe } from '@angular/common';

// Batteries
import { CookieService } from "angular2-cookie/services/cookies.service";
import { AngularMyDatePickerModule } from 'angular-mydatepicker'; // https://github.com/kekeh/angular-mydatepicker

// Custom components
import { AppComponent } from './app.component';
import { CategoriesTableComponent } from './categories-table/categories-table.component';
import { BookerEntriesAppComponent } from './booker-tables-app/booker-tables-app.component';
import { BookerEntrieComponent } from './booker-tables-app/booker-table/booker-table.component';
import { CalculatorComponent } from './calculator/calculator.component';

// Custom services
import { BookerEntriesAPI } from './services/http';
import { CookedSettingsManager } from './services/settingsManager';

// Custom directives
import { smartFloatFieldDirective } from "./services/directives";

// Custom pipes
import { filterObjectsByPropertyPipe } from "./services/pipes";


@NgModule({
  declarations: [
    AppComponent,
    CategoriesTableComponent,
    BookerEntriesAppComponent,
    BookerEntrieComponent,
    smartFloatFieldDirective,
    filterObjectsByPropertyPipe,
    CalculatorComponent,
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AngularMyDatePickerModule
  ],
  providers: [BookerEntriesAPI, CookieService, CookedSettingsManager, DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
