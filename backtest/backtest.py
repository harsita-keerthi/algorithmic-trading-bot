import backtrader as bt
from strategies.moving_average import MovingAverageCrossStrategy
from strategies.mean_reversion import MeanReversionStrategy

def run_backtest(strategy_class):
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy_class)

    # load data
    data = bt.feeds.PandasData