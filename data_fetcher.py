import pandas as pd
from alpaca_trade_api import REST
from config.config import ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL

def fetch_data(symbol, start_date, end_date):
    api = REST(ALPACA_API_KEY, ALPACA_API_SECRET, base_url=ALPACA_BASE_URL)

    # fetch historical data
    bars = api.get_bars(
        symbol,
        timeframe='1D',
        start=start_date,
        end=end_date
    ).df    # convert to pandas data frame

    # rename columns to match naming convention
    bars.reset_index(inplace=True)  # make sure datetime is a column, not index
    bars.rename(columns={'timest, amp': 'datetime'}, inplace=True)

    # return csv
    return bars

if __name__ == '__main__':
    symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2024-02-01'

    # fetch and save data
    data = fetch_data(symbol, start_date, end_date)
    data.to_csv('data/aapl_data.csv')
    print("Data fetched and saved to 'data/aapl_data.csv'")