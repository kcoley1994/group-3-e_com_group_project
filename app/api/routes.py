from flask import Blueprint, request
from app.models import Product

api = Blueprint('api', __name__, url_prefix='/api')


# GET api route
@api.route('/products')
def view_products_api():
    products = Product.query.all()
    products_api = []
    for product in products:
        products_api.append(product.to_dict())
    return{
        "status": "ok",
        "data": products_api
    }

# GET api dinamic route
@api.route('/products/<int:product_id>')
def view_single_product_api(product_id):
    product = Product.query.get(product_id)
    if product:
        return {
            "status": "ok",
            "data": product.to_dict()
        }
    else:
        return {
            "status": "failed",
            "message": "That product does not exist."
        }

# POST api route
@api.route('/products/create', methods=['POST'])
def create_products_api(): 

    # This is coming from POST request body
    data = request.json

    # unpacking data
    name = data["name"]
    img_url = data['img_url']
    price = data['price']
    quantity = data['quantity']
    description = data['description']
    

    # instantiate
    product = Product(name, img_url, price, quantity, description)

    # add product to database
    product.save_to_db()

    return {
        'status': 'ok',
        'message': 'Product was successfully created.'
    }