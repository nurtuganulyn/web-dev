import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Category } from './category';
import { Clothes } from './clothes';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const categories = [
      {id: 1, name: 'Iphone'},
      {id: 2, name: 'Samsung'},
      {id: 3, name: 'Huawei'},
      {id: 4, name: 'Laptops'},
      {id: 5, name: 'Other devices'},
      
    ];
    const clothes = [
      {
        id: 1,
        name: 'Смартфон iPhone 6s 32Gb Space Gray',
        imageLink: 'https://fora.kz/images/content/products/602123/iphone-6s-32gb_58186759dd8db.jpg',
        imageLink2: 'https://fora.kz/images/content/products/602123/iphone-6s-32gb-space-gray_5818690bd10b6.jpg',
        price: '119 890',
        description: ' ',
        category: 1,
      },
      {
        id: 2,
        name: 'Смартфон Samsung Galaxy A01 Blue',
        imageLink: 'https://fora.kz/images/content/products/613204/smartfon-samsung-galaxy-a01-sm-a015fzbdskz-blue_5e2a775d0de12.jpg',
        imageLink2: 'https://fora.kz/images/content/products/613204/smartfon-samsung-galaxy-a01-sm-a015fzbdskz-blue_5e2a775dd5a33.jpg',
        price: '42 590',
        description: '',
        category: 2,
      },
      {
        id: 3,
        name: 'Смартфон iPhone 11 Pro Max 512Gb Space Gray',
        imageLink: 'https://fora.kz/images/content/products/611856/smartfon-apple-iphone-11-pro-max-512gb-space-gray_5d80ae9e6abc7.jpg',
        imageLink2: 'https://fora.kz/images/content/products/611856/smartfon-apple-iphone-11-pro-max-512gb-space-gray_5d80ae9e12e31.jpg',
        price: '919 890',
        description: '',
        category: 1,
      },
      {
        id: 4,
        name: 'Смартфон iPhone Xr 64Gb Black',
        imageLink: 'https://fora.kz/images/content/products/608259/apple-iphone-xr-64gb-black_5bcea6982ccc0.jpg',
        imageLink2: 'https://fora.kz/images/content/products/608259/apple-iphone-xr-64gb-black_5bcea69d458b0.jpg',
        price: '334 890',
        description: '',
        category: 1,
      }, {
        id: 5,
        name: 'Смартфон Samsung Galaxy Z Flip Black',
        imageLink: 'https://fora.kz/images/content/products/613956/smartfon-samsung-galaxy-z-flip-sm-f700fzkdskz-black_5e830b7e38eda.jpg',
        imageLink2: 'https://fora.kz/images/content/products/613956/samsung-galaxy-z-flip-black_5e830f380d15c.jpg',
        price: '699 890',
        description: 'Дизайнеры украсили базовую хлопковую футболку лаконичной надписью \'\'I\'m on a new level.\'\', благодаря которой она выглядит гораздо интереснее. Комбинируйте ее с любым низом, прямой крой подойдет фигуре любого типа.прямой крой\nрукава с отворотами\nуниверсальный цвет',
        category: 2,
      }, {
        id: 6,
        name: 'Смартфон Samsung Galaxy S20+ Blue',
        imageLink: 'https://fora.kz/images/content/products/613393/samsung-galaxy-s20-blue_5e439321282ed.jpg',
        imageLink2: 'https://fora.kz/images/content/products/613393/samsung-galaxy-s20-blue_5e43932096940.jpg',
        price: '436 890',
        description: '',
        category: 2,
      }, {
        id: 7,
        name: 'Смартфон Samsung Galaxy A70 128Gb Black + Наушники',
        imageLink: 'https://fora.kz/images/content/products/610056/samsung-galaxy-a70-128gb-black_5e8440009b350.jpg',
        imageLink2: 'https://fora.kz/images/content/products/610056/samsung-galaxy-a70-black_5ccc0f3118b1c.jpg',
        price: '138 890',
        description: '',
        category: 2,
      },
      {
        id: 8,
        name: 'Смартфон Huawei P30 Pro Breathing Crystal',
        imageLink: 'https://fora.kz/images/content/products/612929/huawei-p30-pro-breathing-crystal_5df1e891a82f6.jpg',
        imageLink2: 'https://fora.kz/images/content/products/612929/huawei-p30-pro-breathing-crystal_5df1e8901a334.jpg',
        description: '',
        category: 3,
        price: '346 990',
      },
      {
        id: 9,
        name: 'Смартфон Huawei P30 Pro Aurora Blue',
        imageLink: 'https://fora.kz/images/content/products/610062/huawei-p30-pro-aurora-blue_5df1e072420d0.jpg',
        imageLink2: 'https://fora.kz/images/content/products/610062/huawei-p30-pro-aurora-blue_5df1e0712650d.jpg',
        price: '346 990',
        description: '',
        category: 3,
      },
      {
        id: 10,
        name: 'Ноутбук Dell Inspiron 3782 (210-AROI)',
        imageLink: 'https://fora.kz/images/content/products/611283/dell-inspiron-3782-210-aroi_5d4a9db018b76.jpg',
        imageLink2: 'https://fora.kz/images/content/products/611283/dell-inspiron-3782-210-aroi_5d4a9dbf601ba.jpg',
        price: '159 900',
        description: '',
        category: 4,
      },
      {
        id: 11,
        name: 'Ноутбук Dell Vostro 5581 (210-AQZB_7)',
        imageLink: 'https://fora.kz/images/content/products/611073/dell-vostro-5581-210-aqzb7_5d2ecb3bc00cd.jpg',
        imageLink2: 'https://fora.kz/images/content/products/611073/dell-vostro-5581-210-aqzb7_5d2ecb3135881.jpg',
        price: '289 900',
        description: '',
        ategory: 4,
      },
      {
        id: 12,
        name: 'Ноутбук Asus X543UA-DM2074 (90NB0HF7-M38470)',
        imageLink: 'https://fora.kz/images/content/products/612373/asus-x543ua-dm2074-90nb0hf7-m38470_5ddb8221ba9d9.jpg',
        imageLink2: 'https://fora.kz/images/content/products/612373/asus-x543ua-dm2074-90nb0hf7-m38470_5ddb822170c32.jpg',
        price: '229 900',
        description: '',
        category: 4,
      },
      {
        id: 13,
        name: 'Подставка охлаждения для ноутбука Deepcool N2000 IV',
        imageLink: 'https://fora.kz/images/content/products/3649/deepcool-n2000-iv_59ccca5585b16.jpg',
        imageLink2: 'https://fora.kz/images/content/products/3649/deepcool-n2000-iv_59ccca529811e.jpg',
        price: '7 490',
        description: '',
        category: 5,
      },
      {
        id: 14,
        name: 'Сумка для ноутбука HP Omen Gaming Backpack',
        imageLink: 'https://fora.kz/images/content/products/605664/hp-omen-gaming-backpack_59d206c76e86b.jpg',
        imageLink2: 'https://fora.kz/images/content/products/605664/hp-omen-gaming-backpack_59d206c76e86b.jpg',
        price: '17 990',
        description: '',
        category: 5,
      },
      {
        id: 15,
        name: 'Смартфон Huawei Y6 2019 Black',
        imageLink: 'https://fora.kz/images/content/products/609510/huawei-y6-2019-black_5c8a1fae33480.jpg',
        imageLink2: 'https://fora.kz/images/content/products/609510/huawei-y6-2019-black_5c8a1fb0b7142.jpg',
        price: '49 490',
        description: '',
        category: 3,
      },
    

    ];

    return {categories, clothes};
  }
  
  genId<T extends Category | Clothes>(myTable: T[]): number {
    return myTable.length > 0 ? Math.max(...myTable.map(t => t.id)) + 1 : 11;
  }
}
