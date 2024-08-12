import backtrader as bt

class MeanReversionStrategy(bt.Strategy):
    params = (("window", 20), ("z_score_threshold", -1))

    def __init__(self):
        self.rolling_mean = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.window)
        self.rolling_stf = bt.indicators.StandardDeviation(self.data.close, period=self.params.window)
        self.z_score = (self.data.close - self.rolling_mean) / self.rolling_std

    def next(self):
        if self.z_score < self.params.z_score_threshold:
            if not self.position:
                self.buy()
        elif self.z_score > -self.params.z_score_threshold:
            if self.position:
                self.sell()