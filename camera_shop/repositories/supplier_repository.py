from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier


def save(supplier):
    sql = "INSERT INTO suppliers (name) VALUES ( %s ) RETURNING id"
    values = [supplier.name]
    results = run_sql(sql, values)
    supplier.id = results[0]['id']
    return supplier


def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)
    for row in results:
        supplier = Supplier(row['name'], row['id'])
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['name'], result['id'])
    return supplier


def suppliers_for_product(product):
    suppliers = []

    sql = "SELECT suppliers.* FROM suppliers INNER JOIN suppliers_products ON suppliers_products.supplier_id = suppliers.id WHERE product_id = %s"
    values = [product.id]
    results = run_sql(sql, values)

    for row in results:
        supplier = Supplier(row['name'], row['id'])
        suppliers.append(supplier)
    return suppliers
    
def update(supplier):
    sql = "UPDATE suppliers SET name = %s WHERE id = %s"
    values = [supplier.name, supplier.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)