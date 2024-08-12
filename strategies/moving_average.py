import backtrader as bt

class MovingAverageCrossStrategy(bt.Strategy):
    params = (("short_window", 40), ("long_window", 100))

    def __init__(self):
        self.short_mavg = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.short_window)
        self.long_mavg = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.long_window)

    def next(self):
        if self.short_mavg > self.long_mavg:
            if not self.position:
                self.buy()
        elif self.short_mavg < self.long_mavg:
            if self.position:
                self.sell()