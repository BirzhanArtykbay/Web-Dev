import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CompanyService } from '../../services/company.service';
import { Company} from '../../interfaces/company';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent {
  companies: Company[] = [];

  constructor(private companyService: CompanyService) {
    this.companyService.getCompanies().subscribe(companies => {
      this.companies = companies;
    });
  }
}
