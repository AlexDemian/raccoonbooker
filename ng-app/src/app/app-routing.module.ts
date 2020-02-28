import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BookerTablesAppComponent } from './booker-tables-app/booker-tables-app.component';
import { CategoriesTableComponent } from './categories-table/categories-table.component';


const routes: Routes = [
  { path: 'bookerTables', component: BookerTablesAppComponent },
  { path: 'categoriesTable', component: CategoriesTableComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
