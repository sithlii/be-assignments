from flask import Blueprint
from controllers import product_controller

product = Blueprint('product', __name__)

@product.route('/product', methods=['POST'])
def create_product():
    return product_controller.create_product()

@product.route('/products', methods=['GET'])
def get_products():
    return product_controller.get_products()

@product.route('/products/active', methods=['GET'])
def get_active_products():
    return product_controller.get_active_products()

@product.route('/products/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return product_controller.get_product_by_id(product_id)

@product.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    return product_controller.update_product(product_id)

@product.route('/product/activity/<product_id>', methods=['PUT'])
def product_activity(product_id):
    return product_controller.product_activity(product_id)

@product.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    return product_controller.delete_product(product_id)