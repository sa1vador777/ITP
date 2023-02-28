import csv

def main() -> str:

    with open("data_17.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        main_list = sorted(reader, key=lambda x: float(x['Price'][1:]))

        tasty_prices, tasteless_prices, unknown_prices = [], [], []
        out_of_date, prices = [], []
        out_of_date_count = 0

        for row in main_list:
            prices.append(float(row['Price'][1:]))

            if row['Category'] == 'Невкусные':
                tasteless_prices.append(float(row['Price'][1:]))
            if row['Category'] == 'Вкусные':
                tasty_prices.append(float(row['Price'][1:]))
            if row['Category'] == 'Неизвестно':
                unknown_prices.append(float(row['Price'][1:]))
        
        max_price = max(prices)
        
        for row in main_list:
            if row['Price'] == f'${max_price}':
                max_price_product = row['Product']

        for row in main_list:
            if row['OutOfDate'] == 'false':
                out_of_date.append(float(row['Price'][1:]))
                out_of_date_count += 1

        print(f'Средняя цена:\nНевкусные: ${sum(tasteless_prices)/len(tasteless_prices)}; Вкусные: ${sum(tasty_prices)/len(tasty_prices)}; Неизвестно: ${sum(unknown_prices)/len(unknown_prices)}')
        print(f'Товар с макисмальной ценой: {max_price_product}')
        print(f'Количество непросроченных товаров: {out_of_date_count}; их суммарная цена: {sum(out_of_date)}')

if __name__ == '__main__':
    main()
