from flask import Flask, request
from binance.client import Client
import os

app = Flask(__name__)

API_KEY = os.environ.get("BINANCE_KEY")
API_SECRET = os.environ.get("BINANCE_SECRET")

client = Client(API_KEY, API_SECRET)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    action = data.get("action")
    symbol = data.get("symbol")
    qty = float(data.get("qty"))

    if action == "buy":
        order = client.order_market_buy(symbol=symbol, quantity=qty)
    elif action == "sell":
        order = client.order_market_sell(symbol=symbol, quantity=qty)
    else:
        return {"status": "erro", "msg": "ação inválida"}

    return {"status": "sucesso", "ordem": order}

if __name__ == "__main__":
    app.run()
