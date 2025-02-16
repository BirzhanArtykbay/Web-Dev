
import { Component, OnInit } from '@angular/core';
import { Product } from '../model/product.interface';
import { ProductsService } from '../services/products.service';
import {CurrencyPipe, NgForOf} from '@angular/common';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  imports: [
    CurrencyPipe,
    NgForOf,

  ],
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  products: Product[] = [];
  currentImageIndex: number = 0;

  constructor(private productsService: ProductsService) {}

  ngOnInit(): void {
    this.products = this.productsService.getProducts();
  }

  shareWhatsApp(product: Product): void {
    const text = encodeURIComponent(`Check out this product: ${product.name}\n${product.kaspiLink}`);
    window.open(`https://wa.me/?text=${text}`, '_blank');
  }

  shareTelegram(product: Product): void {
    const text = encodeURIComponent(`Check out this product: ${product.name}\n${product.kaspiLink}`);
    window.open(`https://t.me/share/url?url=${product.kaspiLink}&text=${text}`, '_blank');
  }

  nextImage(product: Product, index: number): void {
    product.currentImageIndex = ((product.currentImageIndex || 0) + 1) % product.images.length;
  }

  prevImage(product: Product, index: number): void {
    const totalImages = product.images.length;
    const currentIndex = product.currentImageIndex || 0;
    product.currentImageIndex = (currentIndex + totalImages - 1) % totalImages;
  }

}
