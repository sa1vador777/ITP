import csv

def main() -> str:

    with open("data_05.csv", encoding='utf-8') as file:

        reader = csv.DictReader(file, delimiter=',')
        main_list = sorted(reader, key=lambda x: float(x['Price'][1:]))

        moscow_prices, stavropol_prices, voronezh_prices, rostov_prices = [], [], [], []
        stavropol_count = 0
        male_count, female_count = 0, 0
        equal_points = 0

        for row in main_list:
            if row['City_From'] == 'Moscow':
                moscow_prices.append(float(row['Price'][1:]))
            elif row['City_From'] == 'Stavropol':
                stavropol_prices.append(float(row['Price'][1:]))
                stavropol_count += 1
            elif row['City_From'] == 'Voronezh':
                voronezh_prices.append(float(row['Price'][1:]))
            elif row['City_From'] == 'Rostov-on-Don':
                rostov_prices.append(float(row['Price'][1:]))

        for row in main_list:
            if row['Gender'] == 'M':
                male_count += 1
            else:
                female_count += 1
        
        for row in main_list:
            if row['City_From'] == row['City_To']:
                equal_points += 1
        
        print(f'Кол-во билетов из Ставрополя: {stavropol_count}')
        print(f'Средняя цена билета для:\nМосквы: {sum(moscow_prices)/len(moscow_prices)}; Ставрополя: {sum(stavropol_prices)/len(stavropol_prices)}; Воронежа: {sum(voronezh_prices)/len(voronezh_prices)}; Ростова: {sum(rostov_prices)/len(rostov_prices)}')
        print(f'Кол-во билетов, купленных мужчинами: {male_count}; женщинами: {female_count}')
        print(f'Кол-во билетов с одинаковыми пунктами отправления и прибытия: {equal_points}')

if __name__ == '__main__':
    main()
