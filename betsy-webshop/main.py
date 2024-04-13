# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line
from models import *

# Connect to the database
db.connect()


def search(term):
    try:
        #search for products with names containing the given term(case-insentitive)
        products=Product.select().where(Product.name **f'%{term}%')
        #print the result
        if products:
            print(f"Products containing '{term}':")
            for product in products:
                # print(f"ID: {product.product_id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Stock: {product.quantity_description_amount_in_stock}")
                print(f"ID:{product.product_id}, Name:{product.name},Description:{product.description},Price:{product.price},Stock:{product.quantity_description_amount_in_stock}")
        else:
            #print(f"No products found containing '{term}'")
             print(f"No products found containing'{term}'")

    except Exception as e:
        print(f"Error occurred: {e}")

def list_user_products(user_id):
    try:
        #retrieve the user from the database
        user=User.get(User.user_id==user_id)
        
        #Fetch all products owned by the user
        products=Product.select().where(Product.owner==user)
        list_i=[]
        for product in products:
           list_i.append(product.name) 
        print('product:',list_i)      
        return list_i
    except User.DoesNotExist:
        print( f"User with ID {user_id} does not exist")
        return f"User with ID {user_id} does not exist"
    except Exception as e:
        Print(f"Error:{e}")
        return f"Error:{e}"

def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product_detail):
    try:
        #retrieve the user object from the database
        user=User.get(User.user_id==user_id)
        #create a new product object with the provided details
        new_product=Product.create(
           name=product_detail['name'],
           description=product_detail['description'],
           price=product_detail['price'],
           quantity_description_amount_in_stock=product_detail['quantity_description_amount_in_stock'],
           owner=user
           )
           
        
        db.commit()
        print("Product added succesfully to the catalog.")
        return new_product
    except User.DoesNotExist:
        print(f"User with Id {user_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None



def update_stock(product_id, new_quantity):
    try:
        print("R 64:",product_id,new_quantity)
        product=Product.get(Product.product_id==product_id)#w? 
        # update the amount in stock
        product.quantity_description_amount_in_stock=new_quantity
        print('R 68:product.quantity_description_amount_in_stock',product.quantity_description_amount_in_stock)
        product.save()
        
        print(f"Stock for product with ID {product_id} updated to {new_quantity}")
        return True
    except Product.DoesNotExist:
        print(f"Product with Id {product_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None



def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    try:
        product=Product.get(Product.product_id==product_id)#w? ues
        product_delete=product.delete_instance()
        print(f"Product with Id {product_id} has been removed")

        return product_delete
    except Product.DoesNotExist:
        print(f"Product with Id {product_id} does not exist")
        return None
    except Exception as e:
        print(f"Error occurred:{e}")
        return None

if __name__ == "__main__":
   search("sweater")
  

   pass
   