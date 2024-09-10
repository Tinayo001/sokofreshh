#!/usr/bin/python3

from flask_cors import CORS
from flask import Blueprint, request, jsonify, render_template
from app.models import Farmer, Retailer, Product, Order, Transaction, db

# Blueprint
routes = Blueprint('routes', __name__)

# Home route
@routes.route('/', strict_slashes=False)
def home():
    return render_template('index.html')

# Routes for Farmers
@routes.route('/farmers', methods=['POST'])
def create_farmer():
    data = request.get_json()
    farmer = Farmer(**data)
    db.session.add(farmer)
    db.session.commit()
    return jsonify({'message': 'Farmer created', 'farmer': farmer.id}), 201

@routes.route('/farmers', methods=['GET'])
def get_farmers():
    farmers = Farmer.query.all()
    return jsonify([farmer.as_dict() for farmer in farmers]), 200

@routes.route('/farmers/<int:id>', methods=['PUT'])
def update_farmer(id):
    farmer = Farmer.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(farmer, key, value)
    db.session.commit()
    return jsonify({'message': 'Farmer updated'}), 200

@routes.route('/farmers/<int:id>', methods=['DELETE'])
def delete_farmer(id):
    farmer = Farmer.query.get_or_404(id)
    db.session.delete(farmer)
    db.session.commit()
    return jsonify({'message': 'Farmer deleted'}), 200

# Routes for Retailers
@routes.route('/retailers', methods=['POST'])
def create_retailer():
    data = request.get_json()
    retailer = Retailer(**data)
    db.session.add(retailer)
    db.session.commit()
    return jsonify({'message': 'Retailer created', 'retailer': retailer.id}), 201

@routes.route('/retailers', methods=['GET'])
def get_retailers():
    retailers = Retailer.query.all()
    return jsonify([retailer.as_dict() for retailer in retailers]), 200

# Routes for Products
@routes.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created', 'product': product.id}), 201

@routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.as_dict() for product in products]), 200

# Routes for Orders
@routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order created', 'order': order.id}), 201

@routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.as_dict() for order in orders]), 200

# Routes for Transactions
@routes.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    transaction = Transaction(**data)
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created', 'transaction': transaction.id}), 201

@routes.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.as_dict() for transaction in transactions]), 200

# Register the blueprint
def init_routes(app):
    CORS(app)
    app.register_blueprint(routes)
