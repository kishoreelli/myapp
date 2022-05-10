class side:
    buy = 1
    sell = -1


class productType:
    cnc = 'CNC'
    intraday = 'INTRADAY'
    co = 'CO'
    bo = 'BO'


class order:
    def __init__(self, symbl):
        a = symbl
        self.symbol = "NSE:" + a.upper() + "-EQ"
        self.qty = 1
        self.type = 2
        self.side1 = side.buy
        self.productType1 = productType.cnc
        self.limitPrice = 0
        self.stopPrice = 0
        self.validity = "DAY"
        self.disclosedQty = 0
        self.offlineOrder = "False"
        self.stopLoss = 0
        self.takeProfit = 0
