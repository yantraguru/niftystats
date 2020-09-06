# Contains helper functions for generating nifty statistics

import pandas as pd
import datetime

DATA_DIR = './../data/'
NIFTY_ALL_EOD_DATA_FILE = DATA_DIR + 'nifty_price_data.csv'

OHLC_CONVERSION_DICT = {'Open': 'first',
                        'High': 'max',
                        'Low': 'min',
                        'Close': 'last',
                        'Volume': 'sum'}


def load_nifty_data(start_date=None, end_date=None):
    nifty_data = pd.read_csv(NIFTY_ALL_EOD_DATA_FILE, index_col=["Date"],
                             usecols=["Date", "Open", "High", "Low", 'Close', "Volume"],
                             parse_dates=True)

    if start_date:
        start_date_str = datetime_to_datetime_str(start_date)
    else:
        start_date_str = datetime_to_datetime_str(nifty_data.index.min())

    if end_date:
        end_date_str = datetime_to_datetime_str(end_date)
    else:
        end_date_str = datetime_to_datetime_str(nifty_data.index.max())

    nifty_data_select = nifty_data[start_date_str:end_date_str].copy()
    return nifty_data_select


def datetime_to_datetime_str(date_time):
    return date_time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    nifty_data = load_nifty_data()
    print(nifty_data.index.min(), nifty_data.index.max(), len(nifty_data))

    nifty_data = load_nifty_data(datetime.datetime(2020, 5, 17),datetime.datetime(2020, 6, 17))
    print(nifty_data.index.min(), nifty_data.index.max(), len(nifty_data))

    nifty_data = load_nifty_data(start_date=datetime.datetime(2018, 9, 20))
    print(nifty_data.index.min(), nifty_data.index.max(), len(nifty_data))

    nifty_data = load_nifty_data(end_date = datetime.datetime(2000, 2, 20))
    print(nifty_data.index.min(), nifty_data.index.max(), len(nifty_data))