import backtrader as bt

class RiskManagedStrategy(bt.SignalStrategy):
    params = (('risk_per_trade', 0.01),)    # risk 1% of the portfolio per trade

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data.close, period=20)
        seld.order_size = 0

    def next(self):
        if self.data.clost[0] < self.sma[0]:
            if not self.position:
                risk_amount = self.broker.getValue() * self.params.risk_per_trade
                self.order_size = int(risk_amount / self.data.close[0])
                self.buy(size=self.order_size)
        elif self.data.close[0] > self.sma[0]:
            if self.position:
                self.sell(size=self.order_size)
            