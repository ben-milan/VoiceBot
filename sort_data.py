from test_data import generate_data
import pandas as pd

generate_data()
sectors = ['A', 'B', 'C', 'D']
rows = range(1, 11)
prices = [20, 30, 40, 50]
statuses = ['o', 'c']
test_data_path = 'test_data.csv'


def sort_by_sector():
    sector_input = input('Gib einen oder mehrere Sektoren an [A-D, durch Komma getrennt, ohne Abstand]\n>>> ')
    sector_input = sector_input.upper().split(',')
    while not all(sector in sectors for sector in sector_input):
        print('ERROR: Einer oder mehrere Sektoren existieren nicht!')
        sector_input = input('Gib einen oder mehrere Sektoren an [A-D, durch Komma getrennt, ohne Abstand]\n>>> ')
        sector_input = sector_input.upper().split(',')

    df = pd.read_csv(test_data_path)
    filtered_df = df[df['Sektor'].isin(sector_input)]
    filtered_df.to_csv(test_data_path, index=False)


def sort_by_row():
    row_input = input('Gib eine oder mehrere Reihen an [1-10, durch Komma getrennt, ohne Abstand]\n>>> ')
    row_input = list(map(int, row_input.split(',')))
    while not all(row in rows for row in row_input):
        print('ERROR: Eine oder mehrere Reihen existieren nicht!')
        row_input = input('Gib eine oder mehrere Reihen an [1-10, durch Komma getrennt, ohne Abstand]\n>>> ')
        row_input = list(map(int, row_input.split(',')))

    df = pd.read_csv(test_data_path)
    filtered_df = df[df['Reihe'].isin(row_input)]
    filtered_df.to_csv(test_data_path, index=False)


def sort_by_price():
    price_input = input('Gib einen oder mehrere Preise an [20, 30, 40, 50, durch Komma getrennt, ohne Abstand]\n>>> ')
    price_input = list(map(int, price_input.split(',')))
    while not all(price in prices for price in price_input):
        print('ERROR: Eine oder mehrere Preise existieren nicht!')
        price_input = input(
            'Gib einen oder mehrere Preise an [20, 30, 40, 50, durch Komma getrennt, ohne Abstand]\n>>> ')
        price_input = list(map(int, price_input.split(',')))

    df = pd.read_csv(test_data_path)
    filtered_df = df[df['Preis'].isin(price_input)]
    filtered_df.to_csv(test_data_path, index=False)


def sort_by_status():
    status_input = input('Gib einen oder mehrere Status an [o, c, durch Komma getrennt, ohne Abstand]\n>>> ')
    status_input = status_input.split(',')
    while not all(status in statuses for status in status_input):
        print('ERROR: Eine oder mehrere Status existieren nicht!')
        status_input = input('Gib einen oder mehrere Status an [o, c, durch Komma getrennt, ohne Abstand]\n>>> ')
        status_input = status_input.split(',')

    df = pd.read_csv(test_data_path)
    filtered_df = df[df['Status'].isin(status_input)]
    filtered_df.to_csv(test_data_path, index=False)


def all_sorts():
    sort_by_sector()
    sort_by_row()
    sort_by_price()
    sort_by_status()
    print('done')


all_sorts()
