def format_price(price):
    price = int(price)
    price = str(price)
    
    return 'Цена:' + price + 'руб'

format_price(56.24)
print(format_price(56.24))
