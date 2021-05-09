prices = [86.32, 8.35, 33.1, 38.73, 6, .65, 26.97, 45.26, 48.8, 42.38, 50.03, 12.44, 80.96, 50.92, 76.05]


message = ""
for price in prices:
    rubles, kopecks = (int(price), int(price % 1 * 100))
    str_rubles, str_kopecks = f"00{rubles}"[-2:], f"{kopecks}00"[:2]
    message += f"{str_rubles} руб {str_kopecks} коп, "
print(message)


print(f"ID of price list is {id(prices)}")
prices.sort(reverse=True)
message = ""
for price in prices:
    rubles, kopecks = (int(price), int(price % 1 * 100))
    str_rubles, str_kopecks = f"00{rubles}"[-2:], f"{kopecks}00"[:2]
    message += f"{str_rubles} руб {str_kopecks} коп, "
print(message)
print(f"ID of a sorted price list is {id(prices)}")


new_prices = list(reversed(prices))
message = ""
for price in new_prices:
    rubles, kopecks = (int(price), int(price % 1 * 100))
    str_rubles, str_kopecks = f"00{rubles}"[-2:], f"{kopecks}00"[:2]
    message += f"{str_rubles} руб {str_kopecks} коп, "
print(message)
print(f"ID of a new sorted price list is {id(new_prices)}")


print(f"Prices of the 5 most expensive goods are {prices[:5]}")
