app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
client = Client(API_KEY, API_SECRET)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    pair = data['pair']
    qty = float(data['qty'])
    
    if data['message'] == "BUY":
        order = client.order_market_buy(symbol=pair, quantity=qty)
        return f"BUY {qty} {pair} executat", 200

    if data['message'] == "SELL":
        order = client.order_market_sell(symbol=pair, quantity=qty)
        return f"SELL {qty} {pair} executat", 200

    return "Semnal invalid", 400

if __name__ == '__main__':
    app.run(port=5000)
