import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesTableComponent } from './categories-table/categories-table.component';
import { BookerEntriesAppComponent } from './booker-tables-app/booker-tables-app.component';
import { BookerEntrieComponent } from './booker-tables-app/booker-table/booker-table.component';

import { BookerEntriesAPI } from './services/http';
import { CookieService } from "angular2-cookie/services/cookies.service";
import { smartFloatFieldDirective } from "./services/directives";
import { filterObjectsByPropertyPipe } from "./services/pipes";

@NgModule({
  declarations: [
    AppComponent,
    CategoriesTableComponent,
    BookerEntriesAppComponent,
    BookerEntrieComponent,
    smartFloatFieldDirective,
    filterObjectsByPropertyPipe
  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [BookerEntriesAPI, CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }
