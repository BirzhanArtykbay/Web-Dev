import { Routes } from '@angular/router';
import { CompanyListComponent } from './components/company-list/company-list.component';

export const routes: Routes = [
  { path: '', redirectTo: 'companies', pathMatch: 'full' },
  { path: 'companies', component: CompanyListComponent },
];
