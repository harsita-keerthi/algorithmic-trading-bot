from lumibot.bot import Lumibot
from lumibot.config import Config
from lumibot.strategies.lumibot_moving_average import LumibotMovingAverageCrossStrategy

class MyTradingBot(LumiBot):
    def initialize(self):
        self.set_strategy(LumibotMovingAverageCrossStrategy)
        self.set_config(Config.from_file('lumibot/config/congig.yml'))