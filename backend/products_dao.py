from sql_connection import get_sql_connection
def get_all_products(connection):
    
    cursor = connection.cursor()
    query =( "select products.product_id,products.name, products.unit_id,products.price_per_unit, unit.unite_name from products inner join unit on products.unit_id=unit.unite_id")
    cursor.execute(query)
    response =[]
    for (product_id,name,unit_id,price_per_unit, unite_name) in cursor:
        #print(product_id,name,unit_id,price_per_unit)
        response.append(
            {
                'product_id,name' : product_id,
                'name' : name,
                'unit_id' : unit_id,
                'price_per_unit' : price_per_unit,
                'unite_name' : unite_name 

            }

        )
    
    return response
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query =( "insert into products (name, unit_id, price_per_unit) values (%s, %s, %s)")
    data = (product['product_name'], product ['unit_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

def delete_product(connection , product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id ="+ str(product_id))
    cursor.execute(query)
    connection.commit()
if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 11))