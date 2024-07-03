from app.database import get_db

class Product:

    #constuctor
    def __init__(self,id_product=None,product=None,description=None,price=None,image=None):
        self.id_product=id_product
        self.product=product
        self.description=description
        self.price=price
        self.image=image

    def serialize(self):
        return {
            'id_product': self.id_product,
            'product': self.product,
            'description': self.description,
            'price': self.price,
            'image': self.image
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        rows = cursor.fetchall() #Me devuelve una lista de tuplas

        products = [Product(id_product=row[0], product=row[1], description=row[2], price=row[3], image=row[4]) for row in rows]

        cursor.close()
        return products
        

    @staticmethod
    def get_by_id(product_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products WHERE id_product = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Product(id_product=row[0], product=row[1], description=row[2], price=row[3], image=row[4])
        return None
    
    """
    Insertar un registro si no existe el atributo id_product
    """
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_product:
            cursor.execute("""
                UPDATE products SET product = %s, description = %s, price = %s, img = %s
                WHERE id_product = %s
            """, (self.product, self.description, self.price, self.image, self.id_product))
        else:
            cursor.execute("""
                INSERT INTO products (product, description, price, image) VALUES (%s, %s, %s, %s)
            """, (self.product, self.description, self.price, self.image))
            self.id_product = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM products WHERE id_product = %s", (self.id_product,))
        db.commit()
        cursor.close()
