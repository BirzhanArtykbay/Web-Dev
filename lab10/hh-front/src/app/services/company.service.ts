import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {map, Observable} from 'rxjs';
import { Company} from '../interfaces/company';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private apiUrl = 'http://localhost:8000/api/companies/';

  constructor(private http: HttpClient) {
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<any>('http://127.0.0.1:8000/api/companies/').pipe(
      map(response => response.results)
    );
  }
}
//
//   getCompanyVacancies(id: number): Observable<Vacancy[]> {
//     return this.client.get<Vacancy[]>(`${this.BASE_URL}/companies/${id}/vacancies`);
//   }
// }
