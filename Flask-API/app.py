from flask import Flask, jsonify, request

app = Flask(__name__)

product_records = [
    {
        "product_id": "1",
        "product_name": "Hasbro Gaming Clue Game",
        "description": "One murder... 6 suspects...",
        "price": 9.95,
        "active": True
    },
    {
        "product_id": "2",
        "product_name": "Monopoly Board Game The Classic Edition, 2-8 players",
        "description": "Relive the Monopoly experiences...", 
        "price": 35.50,
        "active": False
    }
]

@app.route('/product', methods=['POST'])
def product():
    data = request.form if request.form else request.get_json()
    product = {}
    product['product_id'] = data['product_id']
    product['product_name'] = data['product_name']
    product['description'] = data['description']
    product['price'] = data['price']
    product_records.append(product)
    return jsonify({"message": f"Product {product['product_name']} has been added to the records"}), 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(product_records), 200

@app.route('/products/active', methods=['GET'])
def get_active_products():
    active_products = [product for product in product_records if product['active']]
    return jsonify(active_products), 200

@app.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            return jsonify(product), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            product['product_name'] = request.form['product_name']
            product['description'] = request.form['description']
            product['price'] = request.form['price']
            return jsonify({"message": f"Product {product_id} has been updated"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

@app.route('/product/activity/<product_id>', methods=['PUT'])
def product_activity(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            if product['active'] == True:
                product['active'] = False
            else:
                product['active'] = True
            return jsonify({"message": f"Product {product_id} has been updated"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

@app.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            product_records.remove(product)
            return jsonify({"message": f"Product {product_id} has been deleted"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086')