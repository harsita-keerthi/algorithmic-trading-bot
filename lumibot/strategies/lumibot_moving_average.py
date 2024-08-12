from lumibot.strategy import LumibotStrategy
import pandas as pd

class LumibotMovingAverageCrossStrategy(LumibotStrategy):
    def __init__(self):
        self.sma_short = self.data.close.rolling(windows=50).mean()
        self.sma_long = self.data.close.rolling(windows=200).mean()
    
    def next(self):
        if self.data.close[-1] < self.sma_short[-1] and self.data.close[-1] > self.sma_long[-1]:
            self.buy()
        elif self.data.close[-1] > self.sma_short[-1] and self.data.close[-1] < self.sma_long[-1]:
            self.sell()