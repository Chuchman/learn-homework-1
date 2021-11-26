"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
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
stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_avg_sale(saled_items):
  total_sum = 0
  for item in saled_items:
    total_sum += item
  sales_avg =  total_sum / len(saled_items)
  return sales_avg 

def aggreg_sum(saled_items):
  aggregated_sum = 0
  for item in saled_items:
   aggregated_sum += item
   return  aggregated_sum






def main():
  for one_product in stock:
    sales_avg = round(count_avg_sale(one_product['items_sold']), 2)
    print(f'Среднее количество продаж для товара (каждого): {one_product["product"]} : {sales_avg}')


  for one_product in stock:
    sales_aggr = round(aggreg_sum(one_product['items_sold']),2)
    print(f'Суммарное количество продаж для каждого товара: {one_product["product"]}: {sales_aggr}')
    


total_avg_sum = 0
for one_product in stock:
  sales_avg = count_avg_sale(one_product['items_sold'])
  total_avg_sum += sales_avg
  total_avg = round(total_avg_sum / len("product"), 2)
print(f'Среднее количество продаж всех товаров : {total_avg}')

total_agg_sum = 0
for one_product in stock:
  sales_aggr = aggreg_sum(one_product['items_sold'])
  total_agg_sum += sales_aggr

print(f'Суммарное количество продаж всех товаров: {total_agg_sum}.')









if __name__ == "__main__":
  main()
