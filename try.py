from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

cart_items = []
total_price = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item = request.json
    name = item['name']
    price = item['price']
    cart_items.append({'name': name, 'price': price})
    update_total_price()
    return jsonify({'message': 'Item added to cart successfully.'})


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_index = request.json
    item = cart_items.pop(item_index)
    total_price -= item['price']
    update_total_price()
    return jsonify({'message': 'Item removed from cart successfully.'})


def update_total_price():
    global total_price
    total_price = sum(item['price'] for item in cart_items)


if __name__ == '__main__':
    app.run(debug=True)
