from flask import jsonify, request
from app.models import Product

def index():
    return '<h1>Api lista para servirte con el poder de Python 🐍</h1>'

def get_all_products():
    products = Product.get_all()
    list_products = [product.serialize() for product in products]
    return jsonify(list_products)

def create_product():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    new_product = Product(
        product=data['product'],
        description=data['description'],
        price=data['price'],
        image=data['image']
    )
    new_product.save()
    return jsonify({'message':'Producto ingresado con exito'}), 201
    
def update_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    product.product = data['product']
    product.description = data['description']
    product.price = data['price']
    product.image = data['image']
    product.save()
    return jsonify({'message': 'Producto actualizado con exito'})

def get_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404
    return jsonify(product.serialize())

def delete_product(product_id):
    product = Product.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'Producto no encontrado'}), 404
    product.delete()
    return jsonify({'message': 'Producto borrado con exito'})