from flask import Flask, Blueprint, render_template, request, redirect
from models.product import Product
import repositories.product_repository as product_repository


products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)