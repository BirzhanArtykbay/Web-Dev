import { Component , Input , Output , EventEmitter} from '@angular/core';
import { Product} from '../models';
import {ProductItemComponent} from '../product-item/product-item.component';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  imports: [CommonModule,
    ProductItemComponent
  ],
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  @Input() products: Product[] = [];
  @Output() productRemoved = new EventEmitter<Product>();

  removeProduct(product: Product) {
    this.productRemoved.emit(product);
  }
}
