from AlgorithmImports import *
import json
import os

class MovingAverageCrossStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2023, 1, 1)
        
        self.AddEquity("SPY", Resolution.Daily)
        
        filename = __file__  # e.g., main.py
        strategy_path = os.path.dirname(os.path.abspath(filename))
        param_path = os.path.join(strategy_path, "params.json")
        # Load parameters from JSON
        with open(param_path, "r") as f:
            params = json.load(f)

        self.short_window = int(params.get("short_window", 10))
        self.long_window = int(params.get("long_window", 30))

        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.short_ma = self.SMA(self.symbol, self.short_window, Resolution.Daily)
        self.long_ma = self.SMA(self.symbol, self.long_window, Resolution.Daily)
        self.SetCash(int(params.get("starting_cash", 100000)))
        self.last_action = None

    def OnData(self, data):
        if not self.short_ma.IsReady or not self.long_ma.IsReady:
            return

        holdings = self.Portfolio[self.symbol].Quantity

        if self.short_ma.Current.Value > self.long_ma.Current.Value:
            if holdings <= 0:
                self.SetHoldings(self.symbol, 1.0)
                self.last_action = "BUY"
        elif self.short_ma.Current.Value < self.long_ma.Current.Value:
            if holdings >= 0:
                self.SetHoldings(self.symbol, -1.0)
                self.last_action = "SELL"
