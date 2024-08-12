import sys
import os

import backtrader as bt
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strategies.moving_average import MovingAverageCrossStrategy
from strategies.mean_reversion import MeanReversionStrategy

def run_backtest(strategy_class):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy_class)

    # load data
    data = pd.read_csv('data/aapl_data.csv')
    data.rename(columns={'timestamp': 'datetime'}, inplace=True)

    data['datetime'] = pd.to_datetime(data['datetime'])
    data.set_index('datetime', inplace=True)

    bt_data=bt.feeds.PandasData(dataname=data)
    
    cerebro.adddata(bt_data)
    cerebro.run()
    cerebro.plot()

if __name__ == '__main__':
    run_backtest(MovingAverageCrossStrategy)