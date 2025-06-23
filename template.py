"""
json prob look like this 
{
    indicators:[
        {id:string, name:string, symbol:string, value:int or float},
        ...
    ]
    rules:[
        {id:string, name:string, strategy:string, comparison:(<,>,==), value:int or float}
    ]

}
"""

class strategies():
    def __init__(self):
        self.indicators = ""
        self.rules = ""
        self.template = """
        class MyAlgo(QCAlgorithm):
            def Initialize(self):
                self.SetStartDate(2021, 1, 1)
                self.SetEndDate(2021, 12, 31)
                self.AddEquity("SPY", Resolution.Daily)
        {indicators}

            def OnData(self, data):
        {rules}
        """
    def addIndicators(self, json_input):
        if not json_input["indicators"]:
            raise Exception
        else:
            for ind in json_input["indicators"]:
                self.indicators += f"       self.{ind['id']} = self.{ind['name']}('{ind['symbol']}', {ind['value']})\n"
    
    def addRules(self, json_input):
        if not json_input["rules"]:
            raise Exception
        else:
            for rule in json_input["rules"]:
                tag = f"self.{rule['id']}"
                condition = f"{rule["comparison"]} {rule["value"]}"
                pass
