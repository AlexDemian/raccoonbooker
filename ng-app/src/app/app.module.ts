import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CategoriesTableComponent } from './categories-table/categories-table.component';
import { BookerTablesAppComponent } from './booker-tables-app/booker-tables-app.component';
import { BookerTableComponent } from './booker-tables-app/booker-table/booker-table.component';

import { BookerEntriesAPI } from './services/http';

@NgModule({
  declarations: [
    AppComponent,
    CategoriesTableComponent,
    BookerTablesAppComponent,
    BookerTableComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [BookerEntriesAPI],
  bootstrap: [AppComponent]
})
export class AppModule { }
