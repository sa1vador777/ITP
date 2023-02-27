import csv

def main() -> str:

    with open("data_03.csv") as file:

        reader = csv.DictReader(file, delimiter=',')     
        main_list = sorted(reader, key=lambda x: float(x['Price'][1:]))

        microsoft_prices, MKS_prices, nestle_prices, craft_prices  = [], [], [], []
        microsoft_count, MKS_count, nestle_count, craft_count = [], [], [], []
        out_of_date = []

        for row in main_list:
            if row['Company'] == 'Microsoft':
                microsoft_prices.append(float(row['Price'][1:]))
                microsoft_count.append(int(row['Count']))
            if row['Company'] == 'MKS':
                MKS_prices.append(float(row['Price'][1:]))
                MKS_count.append(int(row['Count']))
            if row['Company'] == 'Nestle':
                nestle_prices.append(float(row['Price'][1:]))
                nestle_count.append(int(row['Count']))
            if row['Company'] == 'Craft Ltd':
                craft_prices.append(float(row['Price'][1:]))
                craft_count.append(int(row['Count']))
        
        for row in main_list:
            if float(row['Price'][1:]) == max(microsoft_prices):
                microsoft_max = row['Product']
            if float(row['Price'][1:]) == max(MKS_prices):
                MKS_max = row['Product']
            if float(row['Price'][1:]) == max(nestle_prices):
                nestle_max = row['Product']
            if float(row['Price'][1:]) == max(craft_prices):
                craft_max = row['Product']
        
        for row in main_list:
            if int(row['Count']) == min(microsoft_count):
                microsoft_min = row['Product']
            if int(row['Count']) == min(MKS_count):
                MKS_min = row['Product']
            if int(row['Count']) == min(nestle_count):
                nestle_min = row['Product']
            if int(row['Count']) == min(craft_count):
                craft_min = row['Product']

        for row in main_list:
            if row['OutOfDate'] == 'true':
                out_of_date.append(float(row['Price'][1:]))
        
        print(f'Самый дорогой товар:\nMicrosoft: {microsoft_max}; MKS: {MKS_max}; Nestle: {nestle_max}; Craft Ltd: {craft_max}')
        print(f'Товар с минимальным количеством:\nMicrosoft: {microsoft_min}; MKS: {MKS_min}; Nestle: {nestle_min}; Craft Ltd: {craft_min}')
        print(f'Объем просроченной продукции в валюте: ${sum(out_of_date)}')
        print(f'Средняя цена у поставщика:\nMicrosoft: ${sum(microsoft_prices)/len(microsoft_prices)}; MKS: ${sum(MKS_prices)/len(MKS_prices)}; Nestle: ${sum(nestle_prices)/len(nestle_prices)}; Craft Ltd: ${sum(craft_prices)/len(craft_prices)}')        

if __name__ == '__main__':
    main()
