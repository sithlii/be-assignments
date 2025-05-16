from flask import request, jsonify
from data import product_records

def create_product():
    data = request.form if request.form else request.get_json()
    product = {}
    product['product_id'] = data['product_id']
    product['product_name'] = data['product_name']
    product['description'] = data['description']
    product['price'] = data['price']
    product['active'] = data.get('active', True)  # Default to True if not provided
    product_records.append(product)
    return jsonify({"message": f"Product {product['product_name']} has been added to the records"}), 201

def get_products():
    return jsonify(product_records), 200

def get_active_products():
    active_products = [product for product in product_records if product['active']]
    return jsonify(active_products), 200

def get_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            return jsonify(product), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

def update_product(product_id):
    data = request.form if request.form else request.get_json()
    
    for product in product_records:
        if product['product_id'] == product_id:
            if 'product_name' in data:
                product['product_name'] = data['product_name']
            if 'description' in data:
                product['description'] = data['description']
            if 'price' in data:
                try:
                    product['price'] = float(data['price'])
                except (ValueError, TypeError):
                    return jsonify({"error": "Price must be a number"}), 400
            if 'active' in data:
                product['active'] = data['active']
            return jsonify({"message": f"Product {product_id} has been updated"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

def product_activity(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            if product['active'] == True:
                product['active'] = False
            else:
                product['active'] = True
            return jsonify({"message": f"Product {product_id} has been updated"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404

def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            product_records.remove(product)
            return jsonify({"message": f"Product {product_id} has been deleted"}), 200
    return jsonify({"message": f"Product {product_id} not found"}), 404
