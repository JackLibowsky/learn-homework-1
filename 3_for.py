"""

Домашнее задание №1

Цикл for: Продажи товаров

[
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

def count_phone_avg(shop):
    shop_sum = 0
    for item_sold in shop:
    		shop_sum += item_sold
    return shop_sum / len(shop)

products_avg_sum = 0
for one_phone in sales:
    shop_avg = round (count_phone_avg(one_phone['items_sold']), 3)
    print(f'Среднее количество продаж {one_phone["product"]}: {shop_avg}')
    products_avg_sum += shop_avg

product_avg = round (products_avg_sum / len(sales), 2)
print(f'Среднее количество продаж всех товаров: {product_avg}')


