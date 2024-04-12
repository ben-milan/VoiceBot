from test_data import generate_data
import pandas as pd
from AudioProccessing import speak_text, listen_text
generate_data()
sectors = ['A', 'B', 'C', 'D']
rows = range(1, 11)
prices = [20, 30, 40, 50]
statuses = ['1', '2']
test_data_path = 'test_data.csv'


def sort_by_sector():
    sector_input = input('Gib einen oder mehrere Sektoren an [A-D]\n>>> ')
    if sector_input != '*':
        sector_input = sector_input.upper().split(',')
        while not all(sector in sectors for sector in sector_input):
            print('ERROR: Einer oder mehrere Sektoren existieren nicht!')
            sector_input = input('Gib einen oder mehrere Sektoren an [A-D]\n>>> ')
            sector_input = sector_input.upper().split(',')

        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Sektor'].isin(sector_input)]
        filtered_df.to_csv(test_data_path, index=False)
    else:
        print('Alle Sektoren ausgewählt.')


def sort_by_row():
    row_input = input('Gib eine oder mehrere Reihen an [1-10]\n>>> ')
    if row_input != '*':
        try:
            row_list = list(map(int, row_input.split(',')))
            while not all(row in rows for row in row_list):
                print('ERROR: Eine oder mehrere Reihen existieren nicht!')
                row_input = input('Gib eine oder mehrere Reihen an [1-10]\n>>> ')
                row_list = list(map(int, row_input.split(',')))

            df = pd.read_csv(test_data_path)
            filtered_df = df[df['Reihe'].isin(row_list)]
            filtered_df.to_csv(test_data_path, index=False)
        except ValueError:
            print('ERROR: Ungültige Eingabe. Bitte geben Sie ganze Zahlen getrennt durch Komma ein.')
            sort_by_row()
    else:
        print('Alle Reihen ausgewählt.')


def sort_by_price():
    price_input = input('Gib einen oder mehrere Preise an [20, 30, 40, 50]\n>>> ')
    if price_input != '*':
        try:
            price_list = list(map(int, price_input.split(',')))
            while not all(price in prices for price in price_list):
                print('ERROR: Eine oder mehrere Preise existieren nicht!')
                price_input = input(
                    'Gib einen oder mehrere Preise an [20, 30, 40, 50]\n>>> ')
                price_list = list(map(int, price_input.split(',')))

            df = pd.read_csv(test_data_path)
            filtered_df = df[df['Preis'].isin(price_list)]
            filtered_df.to_csv(test_data_path, index=False)
        except ValueError:
            print('ERROR: Ungültige Eingabe. Bitte geben Sie ganze Zahlen getrennt durch Komma ein.')
            sort_by_price()
    else:
        print('Alle Preise ausgewählt.')


def sort_by_status():
        df = pd.read_csv(test_data_path)
        filtered_df = df[df['Status'].isin(['Verfügbar'])]
        filtered_df.to_csv(test_data_path, index=False)



def sort_by_seat():
    seat_input = input('Gib einen oder mehrere Plätze an [1-20]\n>>> ')
    if seat_input != '*':
        try:
            seat_list = list(map(int, seat_input.split(',')))
            while not all(seat in range(1, 21) for seat in seat_list):
                print('ERROR: Eine oder mehrere Plätze existieren nicht!')
                seat_input = input(
                    'Gib einen oder mehrere Plätze an [1-20]\n>>> ')
                seat_list = list(map(int, seat_input.split(',')))

            df = pd.read_csv(test_data_path)
            filtered_df = df[df['Platz'].isin(seat_list)]
            filtered_df.to_csv(test_data_path, index=False)
        except ValueError:
            print('ERROR: Ungültige Eingabe. Bitte geben Sie ganze Zahlen getrennt durch Komma ein.')
            sort_by_seat()
    else:
        print('Alle Plätze ausgewählt.')


def all_sorts():
    print('Wenn mehrere Daten angegeben werden, mit Komma und ohne Abstand abgeben')
    print('Für alle Daten jeweils (*) angeben')
    sort_by_sector()
    sort_by_row()
    sort_by_seat()
    sort_by_price()
    sort_by_status()
    print('Fertig')


all_sorts()
