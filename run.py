from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)
CORS(app)

app.route('/', methods=['GET'])(index)
app.route('/api/products/', methods=['GET'])(get_all_products)
app.route('/api/products/<int:product_id>', methods=['GET'])(get_product)
app.route('/api/products/', methods=['POST'])(create_product)
app.route('/api/products/<int:product_id>', methods=['PUT'])(update_product)
app.route('/api/products/<int:product_id>', methods=['DELETE'])(delete_product)

if __name__=='__main__':
    app.run(debug=True)