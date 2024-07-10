"""Script to convert NOAA NCEI County Temp and Preciptation data to CSV"""

import pandas as pd

noaa_code_to_fips_code_state = {
    1: 1,
    2: 4,
    3: 5,
    4: 6,
    5: 8,
    6: 9,
    7: 10,
    8: 12,
    9: 13,
    10: 16,
    11: 17,
    12: 18,
    13: 19,
    14: 20,
    15: 21,
    16: 22,
    17: 23,
    18: 24,
    19: 25,
    20: 26,
    21: 27,
    22: 28,
    23: 29,
    24: 30,
    25: 31,
    26: 32,
    27: 33,
    28: 34,
    29: 35,
    30: 36,
    31: 37,
    32: 38,
    33: 39,
    34: 40,
    35: 41,
    36: 42,
    37: 44,
    38: 45,
    39: 46,
    40: 47,
    41: 48,
    42: 49,
    43: 50,
    44: 51,
    45: 53,
    46: 54,
    47: 55,
    48: 56,
    50: 2,
}


def convert_to_df(filename):
    df = pd.read_fwf(
        filename,
        widths=[2, 3, 2, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        header=None,
    )
    df.columns = [
        'state_code',
        'county_fips',
        'element',
        'year',
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december',
    ]
    df['state_fips'] = df['state_code'].map(noaa_code_to_fips_code_state)
    df['fips_int'] = (df['state_fips'] * 1000 + df['county_fips']).astype(int)
    df['fips_str'] = df['fips_int'].apply(lambda x: f'{x:05}')
    return df


if __name__ == '__main__':
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('-o', '--output-format', default='csv', choices=['csv', 'parquet'])
    args = parser.parse_args()

    my_file = Path(args.file_name)

    df = convert_to_df(my_file)
    if args.output_format == 'csv':
        new_file = my_file.with_suffix('.csv')
        df.to_csv(new_file, index=False)
    elif args.output_format == 'parquet':
        new_file = my_file.with_suffix('.parquet')
        df.to_parquet(new_file, index=False)
