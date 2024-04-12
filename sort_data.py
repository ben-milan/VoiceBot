from test_data import generate_data
import pandas as pd

generate_data()
sectors = ['A', 'B', 'C', 'D']
rows = range(1, 11)
prices = [20, 30, 40, 50]
statuses = ['1', '2']
seats = range(1, 21)
test_data_path = 'test_data.csv'


def sort_by_sector(sector_input):
    if '*' not in sector_input:
        sector_input = sector_input.upper().split(',')
        while not all(sector in sectors for sector in sector_input):
            print('ERROR: Einer oder mehrere Sektoren existieren nicht!')
            sector_input = input('Gib einen oder mehrere Sektoren an [A-D]\n>>> ')
            sector_input = sector_input.upper().split(',')

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Sektor'].isin(sector_input)]
        filtered_df.to_csv(test_data_path, index=False)


def sort_by_row(row_input):
    if '*' not in row_input:
        row_input = list(map(int, row_input.split(',')))
        while not all(row in rows for row in row_input):
            print('ERROR: Eine oder mehrere Reihen existieren nicht!')
            row_input = input('Gib eine oder mehrere Reihen an [1-10]\n>>> ')
            row_input = list(map(int, row_input.split(',')))

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Reihe'].isin(row_input)]
        filtered_df.to_csv(test_data_path, index=False)


def sort_by_price(price_input):
    if '*' not in price_input:
        price_input = list(map(int, price_input.split(',')))
        while not all(price in prices for price in price_input):
            print('ERROR: Eine oder mehrere Preise existieren nicht!')
            price_input = input(
                'Gib einen oder mehrere Preise an [20, 30, 40, 50]\n>>> ')
            price_input = list(map(int, price_input.split(',')))

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Preis'].isin(price_input)]
        filtered_df.to_csv(test_data_path, index=False)


def sort_by_status(status_input):
    if '*' not in status_input:
        status_input = status_input.split(',')
        while not all(status in statuses for status in status_input):
            print('ERROR: Eine oder mehrere Status existieren nicht!')
            status_input = input(
                'Gib einen oder mehrere Status an [(1): Verfügbar,(2): Besetzt]\n>>> ')
            status_input = status_input.split(',')

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Status'].isin(status_input)]
        filtered_df.to_csv(test_data_path, index=False)


def sort_by_seat(seat_input):
    if '*' not in seat_input:
        seat_input = list(map(int, seat_input.split(',')))
        while not all(seat in seats for seat in seat_input):
            print('ERROR: Eine oder mehrere Sitze existieren nicht!')
            seat_input = input('Gib einen oder mehrere Sitze an [1-20]\n>>> ')
            seat_input = list(map(int, seat_input.split(',')))

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Platz'].isin(seat_input)]
        filtered_df.to_csv(test_data_path, index=False)


def all_sorts():
    print('Wenn mehrere Daten angegeben werden, mit Komma und ohne Abstand abgeben')
    print('Für alle Daten jeweils (*) angeben')
    sector_input = input('Gib einen oder mehrere Sektoren an [A-D]\n>>> ')
    sort_by_sector(sector_input)

    row_input = input('Gib eine oder mehrere Reihen an [1-10]\n>>> ')
    sort_by_row(row_input)

    price_input = input(
        'Gib einen oder mehrere Preise an [20, 30, 40, 50]\n>>> ')
    sort_by_price(price_input)

    status_input = input(
        'Gib einen oder mehrere Status an [(1): Verfügbar,(2): Besetzt]\n>>> ')
    sort_by_status(status_input)

    seat_input = input('Gib einen oder mehrere Sitze an [1-20]\n>>> ')
    sort_by_seat(seat_input)

    print('done')


all_sorts()
