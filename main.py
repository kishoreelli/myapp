from flask import Flask, render_template, request
import pandas as pd
from static.logdata import *

app = Flask(__name__)

"""Home page requests are here"""


@app.route('/')  # index.html HomePage
def hello():
    return render_template('index.html')


@app.route('/charts')  # index.html
def charts():
    return render_template('investing.html')


@app.route('/algotrade')  # index.html to algo.html
def algo():
    return render_template('algo.html', token=access_token)


"""Algo page requests are here"""


@app.route('/algo/auth_code', methods=["GET", "POST"])  # algo.html to auth_code(oneform.html)
def loginToBroker():
    if request.method == "POST":
        result = request.form
        autcodee = result['code']
        token = asscode(autcodee)
        print(token)
        return render_template("oneform.html", info=token, head='Enter token **', link='/token')
    else:
        firstlink()
        return render_template("oneform.html", head='Enter auth_code **', link='/algo/auth_code')


@app.route('/algo/profile')  # algo.html to profile
def profile():
    p = fyers.get_profile()
    print(p)
    df = pd.DataFrame(data=p)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/positions')  # algo.html to trade position
def position():
    p = fyers.positions()
    print(p)
    a = p['netPositions']
    df = pd.DataFrame(data=a)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/holdings')  # algo.html to holdings
def holding():
    p = fyers.holdings()
    print(p)
    a = p['holdings']
    df = pd.DataFrame(data=a)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/funds')  # algo.html to funds
def fund():
    p = fyers.funds()
    print(p)
    a = p['fund_limit']
    df = pd.DataFrame(data=a)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/market_status')  # algo.html to market status
def marketstatus():
    p = fyers.market_status()
    print(p)
    a = p['marketStatus']
    df = pd.DataFrame(data=a)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/orders')  # algo.html to order book
def order():
    p = fyers.orderbook()
    print(p)
    df = pd.DataFrame(data=p)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/minquantity')  # algo.html to min quandtity
def minquanti():
    p = fyers.minquantity()
    print(p)
    a = p['minqtyDict']
    df = pd.DataFrame(data=a)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/tradebook')  # algo.html to trade book
def trade():
    p = fyers.tradebook()
    print(p)
    df = pd.DataFrame(data=p)
    return render_template('displaytable.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/algo/marketbuy', methods=["GET", "POST"])  # algo.html to market Buy(oneform.html)
def mkbuy():
    if request.method == "POST":
        result = request.form
        tg = result['code']
        print(tg)
        return render_template("oneform.html", info=tg, head='buy order placed')
    return render_template("oneform.html", info="Give_input_above", head='Enter Ticker for marketbuy', link='/algo/marketbuy')


@app.route('/algo/marketsell', methods=["GET", "POST"])  # algo.html to market Buy(oneform.html)
def mksell():
    if request.method == "POST":
        result = request.form
        tg = result['code']
        print(tg)
        return render_template("oneform.html", info=tg, head='sell order placed')
    return render_template("oneform.html", info="Give_input_above", head='Enter Ticker for Marketsell', link='/algo/marketsell')


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=8080)
