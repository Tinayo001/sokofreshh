#!/usr/bin/python3

from datetime import datetime, timezone
from app import db

class Farmer(db.Model):
    """
    Represents a farmer in the database.
    
    Attributes:
        id (int): Unique identifier for the farmer.
        name (str): Name of the farmer.
        email (str): Email address of the farmer.
        phone_number (str): Phone number of the farmer.
        location (str): Location of the farmer.
        products (list): List of products associated with this farmer.
    """

    __tablename__ = 'farmers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    
    products = db.relationship('Product', backref='farmer', lazy=True)

    def as_dict(self):
        """
        Convert the model instance to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all attributes of the model.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        """
        Return a string representation of the model instance.
        
        Returns:
            str: String representation of the model instance.
        """
        return f"<Farmer {self.name}>"

class Retailer(db.Model):
    """
    Represents a retailer in the database.
    
    Attributes:
        id (int): Unique identifier for the retailer.
        name (str): Name of the retailer.
        email (str): Email address of the retailer.
        phone_number (str): Phone number of the retailer.
        location (str): Location of the retailer.
        orders (list): List of orders associated with this retailer.
    """

    __tablename__ = 'retailers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    location = db.Column(db.String(150), nullable=False)
    
    orders = db.relationship('Order', backref='retailer', lazy=True)
    
    def as_dict(self):
        """
        Convert the model instance to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all attributes of the model.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        """
        Return a string representation of the model instance.
        
        Returns:
            str: String representation of the model instance.
        """
        return f"<Retailer {self.name}>"

class Product(db.Model):
    """
    Represents a product in the database.
    
    Attributes:
        id (int): Unique identifier for the product.
        name (str): Name of the product.
        description (str): Description of the product.
        price (float): Price of the product.
        quantity (int): Quantity available of the product.
        date_added (datetime): Date when the product was added.
        farmer_id (int): Foreign key referencing the associated farmer.
    """

    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)

    def as_dict(self):
        """
        Convert the model instance to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all attributes of the model.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        """
        Return a string representation of the model instance.
        
        Returns:
            str: String representation of the model instance.
        """
        return f"<Product {self.name}>"

class Order(db.Model):
    """
    Represents an order in the database.
    
    Attributes:
        id (int): Unique identifier for the order.
        quantity (int): Quantity ordered.
        total_price (float): Total price of the order.
        date_ordered (datetime): Date when the order was placed.
        retailer_id (int): Foreign key referencing the associated retailer.
        product_id (int): Foreign key referencing the associated product.
        product (Product): Associated product.
    """

    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date_ordered = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    
    retailer_id = db.Column(db.Integer, db.ForeignKey('retailers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    
    product = db.relationship('Product')

    def as_dict(self):
        """
        Convert the model instance to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all attributes of the model.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        """
        Return a string representation of the model instance.
        
        Returns:
            str: String representation of the model instance.
        """
        return f"<Order {self.id}>"

class Transaction(db.Model):
    """
    Represents a transaction in the database.
    
    Attributes:
        id (int): Unique identifier for the transaction.
        amount (float): Amount of the transaction.
        payment_method (str): Method of payment used.
        date_paid (datetime): Date when the transaction was paid.
        order_id (int): Foreign key referencing the associated order.
        order (Order): Associated order.
    """

    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    date_paid = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    
    order = db.relationship('Order')

    def as_dict(self):
        """
        Convert the model instance to a dictionary representation.
        
        Returns:
            dict: Dictionary containing all attributes of the model.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        """
        Return a string representation of the model instance.
        
        Returns:
            str: String representation of the model instance.
        """
        return f"<Transaction {self.id}>"

