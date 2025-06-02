from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Table, Column, String, Float, select, delete
from typing import List, Optional
from datetime import date
import os


# Initialize Flask app
app = Flask(__name__) # Creates an instance of our flask application.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:test@localhost/ecommerce_api'
# app.config['JWT_SECRET_KEY'] = 'get-swifty'

# Each class in our Model is going to inherit from the Base class, which inherits from the SQLAlchemy base model DeclarativeBase
class Base(DeclarativeBase):
    pass # This class can be further configured but for our use case we don't need to configure it any further, so we're passing.

db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)

#====================== MODELS ==============================================

class Customer(Base):
    
    __tablename__ = 'Customer'
    
    id: Mapped[int] = mapped_column(primary_key=True) # pk
    name: Mapped[str] = mapped_column(db.String(225), nullable=False)
    email: Mapped[str] = mapped_column(db.String(225))
    # password: Mapped[str] = 
    address: Mapped[str] = mapped_column(db.String(225))
    orders: Mapped[List["Orders"]] = db.relationship(back_populates='customer') #back_populates ensures that both ends of the relationship have access to the other
    
# junction table for Orders and Products
order_products = db.Table(
    "Order_Products",
    Base.metadata, #Allows this table to locate the foreign keys from the other Base class
    db.Column('order_id', db.ForeignKey('orders.id')), # fk - orders
    db.Column('product_id', db.ForeignKey('products.id')) # fk - products
)


class Orders(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True) # pk
    order_date: Mapped[date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customer.id')) # fk - customers
    #creating a many-to-one relationship to Customer table
    customer: Mapped['Customer'] = db.relationship(back_populates='orders')
    #creating a many-to-many relationship to Products through or association table order_products
    #we specify that this relationship goes through a secondary table (order_products)
    products: Mapped[List['Products']] = db.relationship(secondary=order_products, back_populates="orders")
    
    shipped_date: Mapped[date] = mapped_column(db.Date, nullable=True)
    delivered_date: Mapped[date] = mapped_column(db.Date, nullable=True)
    
class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True) # pk
    product_name: Mapped[str] = mapped_column(db.String(255), nullable=False )
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    orders: Mapped[List['Orders']] = db.relationship(secondary=order_products, back_populates="products")
    
#============== Initialize the database & create tables ================
with app.app_context():
    # db.drop_all()
    db.create_all()

#============================ SCHEMAS ==================================


# Define Customer Schema
class CustomerSchema(ma.SQLAlchemyAutoSchema): # SQLAlchemyAutoSchemas create schema fields based on the SQLAlchemy model passed in.
    class Meta:
        model = Customer

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Products

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders
        include_fk = True # Need this because Auto Schemas doesn't automatically recognize foreign keys (customer_id)
        
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# =================== API ROUTES (WITH FLASK) ==============
@app.route('/')
def home():
    return "Home"

#=============== API ROUTES: Customer CRUD =================

# Create a customer with a POST request
@app.route("/customers", methods=["POST"])
def add_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], address=customer_data['address'])
    db.session.add(new_customer)
    db.session.commit()
    
    return jsonify({"Message": "New Customer created successfully!",
                    "customer": customer_schema.dump(new_customer)}), 201
    
# Get all customers using a GET method
@app.route("/customers", methods=['GET'])
def get_customers():
    query = select(Customer)
    result = db.session.execute(query).scalars() #Execute query, and convert row objects into scalar objects (python useable)
    customers = result.all() #packs objects into a list
    
    return customers_schema.jsonify(customers), 200

# Get specific customer using a GET method and dynamic route
@app.route("/customers/<int:id>", methods=['GET'])
def get_customer(id):
    query = select(Customer).where(Customer.id == id)
    result = db.session.execute(query).scalars().first() # first() grabs the first object returned
    
    if result is None:
        return jsonify({"Error": "Customer not found"}), 404
    
    return customer_schema.jsonify(result), 200

@app.route("/customers/<int:id>", methods=['PUT'])
def update_customer(id):
    customer = db.session.get(Customer, id)

    if not customer:
        return jsonify({"message": "Invalid customer id"}), 400
    
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.address = customer_data['address']

    db.session.commit()
    return customer_schema.jsonify(customer), 200

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = db.session.get(Customer, id)

    if not customer:
        return jsonify({"message": "Invalid user id"}), 400
    
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": f"succefully deleted customer {id}"}), 200


#=============== API ROUTES: Products CRUD ==================


@app.route('/products', methods=['POST'])
def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_product = Products(product_name=product_data['product_name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"Messages": "New Product added!",
                    "product": product_schema.dump(new_product)}), 201

@app.route("/products", methods=['GET'])
def get_products():
    query = select(Products)
    result = db.session.execute(query).scalars() #Exectute query, and convert row objects into scalar objects (python useable)
    products = result.all() #packs objects into a list
    return products_schema.jsonify(products)

@app.route("/products/<int:id>", methods=['GET'])
def get_product(id):
    query = select(Product).where(Product.id == id)
    result = db.session.execute(query).scalars().first() # first() grabs the first object returned
    
    if result is None:
        return jsonify({"Error": "Product not found"}), 404
    
    return customer_schema.jsonify(result), 200
    

#=============== API ROUTES: Order Operations ==================
#CREATE an ORDER
@app.route('/orders', methods=['POST'])
def add_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    # Retrieve the customer by its id.
    customer = db.session.get(Customer, order_data['customer_id'])
    
    # Check if the customer exists.
    if customer:
        new_order = Orders(order_date=order_data['order_date'], customer_id = order_data['customer_id'])

        db.session.add(new_order)
        db.session.commit()

        return jsonify({"Message": "New Order Placed!",
                        "order": order_schema.dump(new_order)}), 201
    else:
        return jsonify({"message": "Invalid customer id"}), 400

#ADD ITEM TO ORDER
@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['PUT'])
def add_product(order_id, product_id):
    order = db.session.get(Orders, order_id) #can use .get when querying using Primary Key
    product = db.session.get(Products, product_id)
    
    if order and product: #check to see if both exist
        if product not in order.products: #Ensure the product is not already on the order
            order.products.append(product) #create relationship from order to product
            db.session.commit() #commit changes to db
            return jsonify({"Message": "Successfully added item to order."}), 200
        else:#Product is in order.products
            return jsonify({"Message": "Item is already included in this order."}), 400
    else:#order or product does not exist
        return jsonify({"Message": "Invalid order id or product id."}), 400
    
@app.route('/orders/<int:order_id>/add_product/<int:product_id>', methods=['GET'])
def also_ordered(order_id, product_id):
    order = db.session.get(Orders, order_id) #can use .get when querying using Primary Key
    product = db.session.get(Products, product_id)
    
    if order and product:
        other_products = set()
        other_orders = db.session.query(Orders).filter(Orders.id != order_id).all()
        for order in other_orders:
            if product in order.products:
                other_products.update(order.products)
                
    def display_other_products(other_products):
        return "\n".join([f'{product.id}: {product.product_name}' for product in other_products])
    
    return jsonify({"Message": 
        f"\n Other customers have purchased this items along with:\n {display_other_products(other_products)}"}), 200

    
    
@app.route('/orders/<int:order_id>/remove_product/<int:product_id>)', methods=['DELETE'])
def delete_order(order_id, product_id):
    order = db.session.get(Orders, order_id)
    product = db.session.get(Products, product_id)
    
    if order and product:
        if product in order:
            order.products.remove(product)
            db.session.commit()
        return jsonify({"Message": f"{product.product_name} has been successfully removed from order {order.id}, ordered at {order.order_date}."}), 200
    else:
        return jsonify({"Message": "The Product or the Order not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
