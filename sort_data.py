import pandas as pd

sectors = ['A', 'B', 'C', 'D']
test_data_path = 'test_data.csv'


def sort_by_sector():
    sector_input = input('Gib einen Sektor an [A-D]\n>>> ')
    sector_input = sector_input.upper()
    while sector_input not in sectors:
        print('ERROR: Dieser Sektor existiert nicht!')
        sector_input = input('Gib einen Sektor an [A-D]\n>>> ')
        sector_input = sector_input.upper()

    df = pd.read_csv(test_data_path)
    filtered_df = df[df['Sektor'] == sector_input]
    filtered_df.to_csv(test_data_path, index=False)

    print('done')


sort_by_sector()

