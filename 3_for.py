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
sale = [
    {'product': 'iPhone 12', 
    'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 
    'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 
    'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sale_phone(phone_sale):
  score_sum = 0
  for score_phone in phone_sale:
    score_sum += score_phone
  return score_sum

score = len(sale)
num_1 = 0
for len_sale in sale:

  score1 = len(len_sale['items_sold'])
  
print(f'Кол-во обрабатываемых товаров: {score}')
print(f'Кол-во точек- вводных данных по продажам {score1}')

all_sale_phone = 0
for one_phone in sale:
  all_sale = count_sale_phone(one_phone['items_sold'])
  all_sale_phone += all_sale 
  print("По товару:", one_phone["product"],"Общие продажи:", all_sale, "Средние продажи:", all_sale / score1)

print("Общие продажи по всем товарам и всем точкам:", all_sale_phone)
print("Средняя продажа в точке по всем товарам:", all_sale_phone / score1 / score)
  


    
if __name__ == "__count_sale_phone__":
    count_sale_phone(phone_sale)
