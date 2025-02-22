import { Component , Input , Output , EventEmitter} from '@angular/core';
import { Product} from '../models';

@Component({
  selector: 'app-product-item',
  imports: [],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css'
})
export class ProductItemComponent {
  @Input() product!: Product;
  @Output() remove = new EventEmitter<Product>();

  likeProduct() {
    this.product.likes++;
  }

  removeProduct() {
    if (confirm(`Are you sure you want to remove ${this.product.name}?`)) {
      this.remove.emit(this.product);
    }
  }

}
