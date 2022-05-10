from baseorder import *


def marketorderbuy(tiker):
    mo = order(tiker)
    dawe = mo.symbol, mo.qty, mo.type, mo.side1, mo.productType1, mo.limitPrice, mo.stopPrice, \
           mo.validity, mo.disclosedQty, mo.offlineOrder, mo.stopLoss, mo.takeProfit
    data = {"symbol": dawe[0], "qty": dawe[1], "type": dawe[2], "side": dawe[3], "productType": dawe[4],
            "limitPrice": dawe[5], "stopPrice": dawe[6], "validity": dawe[7], "disclosedQty": dawe[8],
            "offlineOrder": dawe[9], "stopLoss": dawe[10], "takeProfit": dawe[11]}
    print(data)
    return data


def marketordersell(tiker):
    mo = order(tiker)
    dawe = mo.symbol, mo.qty, mo.type, side.sell, mo.productType1, mo.limitPrice, mo.stopPrice, \
           mo.validity, mo.disclosedQty, mo.offlineOrder, mo.stopLoss, mo.takeProfit
    data = {"symbol": dawe[0], "qty": dawe[1], "type": dawe[2], "side": dawe[3], "productType": dawe[4],
            "limitPrice": dawe[5], "stopPrice": dawe[6], "validity": dawe[7], "disclosedQty": dawe[8],
            "offlineOrder": dawe[9], "stopLoss": dawe[10], "takeProfit": dawe[11]}
    print(data)
    return data


def limtordersell(tiker, qty):
    mo = order(tiker)
    dawe = mo.symbol, mo.qty, mo.type, side.sell, mo.productType1, mo.limitPrice, mo.stopPrice, \
           mo.validity, mo.disclosedQty, mo.offlineOrder, mo.stopLoss, mo.takeProfit
    data = {"symbol": dawe[0], "qty": qty, "type": dawe[2], "side": dawe[3], "productType": dawe[4],
            "limitPrice": dawe[5], "stopPrice": dawe[6], "validity": dawe[7], "disclosedQty": dawe[8],
            "offlineOrder": dawe[9], "stopLoss": dawe[10], "takeProfit": dawe[11]}
    print(data)
    return data


