# Updates 'NIFTY 50 Price Data.csv' with latest data from NSE website.
# This code uses nsepy library to get the latest NIFTY data

DATA_DIR = './../data/'
NIFTY_EOD_DATA_FILE = DATA_DIR + 'nifty_price_data.csv'
print(NIFTY_EOD_DATA_FILE)

import pandas as pd

from nsepy import get_history

from shutil import copyfile
from datetime import date, timedelta

print('Reading data from NIFTY EOD price data file...')
nifty_data = pd.read_csv(NIFTY_EOD_DATA_FILE, index_col=["Date"],
                         usecols=["Date", "Open", "High", "Low", 'Close', "Volume"],
                         parse_dates=True)
current_data_end_date = nifty_data.index.max().date()
print('NIFTY data is updated till %s' % current_data_end_date)

start_date = nifty_data.index.max().date() + timedelta(1)
end_date = date.today()

print('Connecting for latest data to NSE...')

nifty_update = get_history(symbol='NIFTY', index=True, start=start_date, end=end_date)
nifty_update = nifty_update[['Open', 'High', 'Low', 'Close', 'Volume']]
nifty_update.index = pd.to_datetime(nifty_update.index)

print('New EOD data found with %d rows' % len(nifty_update))

print('Making a backup of existing data file...')
copyfile(NIFTY_EOD_DATA_FILE,NIFTY_EOD_DATA_FILE+'.backup')

print('Merging update data with current data...')
nifty_full_data = pd.concat([nifty_data, nifty_update])

print('Updating data file with current data...')
nifty_full_data.to_csv(NIFTY_EOD_DATA_FILE)

current_data_end_date = nifty_full_data.index.max().date()
print('NIFTY data is now updated till %s' % current_data_end_date)


