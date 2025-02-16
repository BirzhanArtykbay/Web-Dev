// src/app/services/products.service.ts
import { Injectable } from '@angular/core';
import { Product } from '../model/product.interface';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {
  private products: Product[] = [
    {
      id: 1,
      name: 'iPhone 15 Pro Max',
      description: 'Apple iPhone 15 Pro Max 256GB Natural Titanium',
      rating: 4.9,
      price: 638990,
      images: [
        'assets/1.jpeg',
        'assets/2.jpeg',
        'assets/4.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-belyi-113138578/?m=16206714&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_500k&gad_source=1&gbraid=0AAAAAC7-v7hyITjqPHbyaI8XoZN68ipBi&gclid=CjwKCAiAk8G9BhA0EiwAOQxmfsMvQv8YdgVlemH3grR1PmIMWWnkPZ5eEdk_yo50wMb6D_GTcsh3iRoCoI0QAvD_BwE&c=750000000'
    },
    {
      id: 2,
      name: 'Samsung Galaxy S24 Ultra',
      description: 'Samsung Galaxy S24 Ultra 512GB Phantom Black',
      rating: 4.8,
      price: 564900,
      images: [
        'assets/5.jpeg',
        'assets/6.jpeg',
        'assets/7.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/samsung-galaxy-s24-ultra-5g-12-gb-512-gb-chernyi-116044201/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 3,
      name: 'MacBook Pro 16"',
      description: 'Apple MacBook Pro 16-inch M1 Pro 512GB Space Gray',
      rating: 4.9,
      price: 1249990,
      images: [
        'assets/8.jpeg',
        'assets/9.jpeg',
        'assets/10.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/apple-macbook-pro-16-2021-16-2-16-gb-ssd-512-gb-macos-mk183-102892102/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 4,
      name: 'Sony PlayStation 5',
      description: 'Sony PlayStation 5 Slim Disc Edition + CyberPunk77',
      rating: 4.7,
      price: 385509,
      images: [
        'assets/11.jpeg',
        'assets/12.jpeg',
        'assets/13.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/sony-playstation-5-slim-cyberpunk-2077-ultimate-edition-atomic-heart--116600256/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 5,
      name: 'Haier 55 SMART TV S1',
      description: 'Haier 55 SMART TV S1 140-inch black',
      rating: 4.6,
      price: 308000,
      images: [
        'assets/14.jpeg',
        'assets/15.jpeg',
        'assets/16.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/haier-55-smart-tv-s1-140-sm-chernyi-108623778/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 6,
      name: 'Asus ROG Strix RTX 4090',
      description: 'Asus ROG Strix GeForce RTX 4090 OC Edition',
      rating: 4.9,
      price: 1029000,
      images: [
        'assets/17.jpeg',
        'assets/18.jpeg',
        'assets/19.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/asus-rog-strix-g16-16-32-gb-ssd-1000-gb-dos-g614ji-n4181-90nr0d41-m00v20-118060952/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 7,
      name: 'Apple iPad Pro 11"',
      description: 'Apple iPad Pro 11-inch M4 Chip 256GB Space Gray',
      rating: 4.8,
      price: 577000,
      images: [
        'assets/20.jpeg',
        'assets/21.jpeg',
        'assets/22.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/apple-ipad-pro-2024-wi-fi-11-djuim-8-gb-256-gb-serebristyi-119582267/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 8,
      name: 'Sony WH-1000XM5',
      description: 'Sony WH-1000XM5 Wireless Noise Cancelling Headphones',
      rating: 4.9,
      price: 149000,
      images: [
        'assets/23.jpeg',
        'assets/24.jpeg',
        'assets/25.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/sony-wh-1000xm5-chernyi-105259822/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 9,
      name: 'Apple Watch Series 10',
      description: 'Apple Watch Series 10 S/M 42mm Gold',
      rating: 4.7,
      price: 218000,
      images: [
        'assets/26.jpeg',
        'assets/27.jpeg',
        'assets/28.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/apple-watch-series-10-s-m-42-mm-zolotistyi-belyi-128574070/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    },
    {
      id: 10,
      name: 'Dyson V15s Detect',
      description: 'Dyson V15 Detect Submarines Vacuum Cleaner',
      rating: 4.8,
      price: 421000,
      images: [
        'assets/29.jpeg',
        'assets/30.jpeg',
        'assets/31.jpeg'
      ],
      kaspiLink: 'https://kaspi.kz/shop/p/dyson-v15s-detect-submarine-serebristyi-114424216/?c=750000000&utm_source=google&utm_medium=cpc&utm_campaign=shop_google_performance_max_smartphones_v2&gbraid=0AAAAAC7-v7hXMr6FXjhFKekjP3UOThbXr&gclid=CjwKCAiAtsa9BhAKEiwAUZAszSqgE5_yr_pBwEgxwFiwRdsIl9CUC1DG1YQqo7QcLEnZa_QQC3uBLxoCEL4QAvD_BwE'
    }
  ];

  getProducts(): Product[] {
    return this.products;
  }
}
