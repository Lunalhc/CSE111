import csv


def main():

    read_dict("products.csv",0)
    
    # store products file into a dictionary
    products_dict = read_dict("products.csv",0)
    
    print(products_dict)

    with open("request.csv","rt") as csv_file:
        
        # store the request file in reader
        reader = csv.reader(csv_file)

        next(reader)

        for rows in reader:
            # store every product number in request file as a list
            product_number = rows[0]
            # store every product quantity in request file as a list
            quantity = rows[1]
            
            # use the product number in request file to find the product information in products file
            # store it in a list called "products"
            products = products_dict[product_number] 

            # store every name in "products" list as a list
            product_name = products[1]

            # store every price in "products" list as a list
            product_price_each = float(products[2])

            for number in product_number:

                product_quantity = int(quantity)
            
            print(product_name,product_quantity,product_price_each)





def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.

    """
    product_index = 0
    name_index=1
    price_index =2

    with open(filename,"rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        dictionary = {}

        for rows in reader:
            
            key = rows[product_index]

            value1 =rows[name_index]

            value2 = rows[price_index]

            dictionary[key] = [key,value1,value2]

    return dictionary





if __name__ =="__main__":

    main()