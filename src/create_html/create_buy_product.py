#To succesfuslly invoke the function 'get_all_data_from_accessories', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_accessories import get_all_data_from_accessories
from pathlib import Path
from os import getcwd as getCurrentDirectory

def create_buy_product():
    
    try:
        #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/buy-products.html'.
        working_directory = Path(getCurrentDirectory())
        path = working_directory / "docs" / "buy-product.html"

        #Opens the file with the purpose to write on it.
        file = path.open('w', encoding="utf-8")

        #Saves the html content into the variable 'html'.
        html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Rental Bike - Buy a Product</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="author" content="Samuel_Piedra and Noa_Cocaña">
        <meta name="description" content="rent bicycle page">
        <meta name="copyright" content="Samu&Noa">
        <meta name="generator" content="VisualStudioCode">
        <meta name="keywords" content="rent, accesories, shops, bikes, bicycles, type of bicycle">
        <meta http-equiv="content-language" content="text_EN">
        <link rel="stylesheet" href="./css/styles-main.css">
        <link rel="stylesheet" href="./css/styles-buy-product.css">
        <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
        <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
        <base target="_self">
    </head>
    <body id="background-buying">
        <div class="index-footer">
            <header>
                <div class="container-header">
                    <div class="container-header-logo">
                        <img src="./img/logo-webpage.png" height="65px" width="90px" alt="rental logo">  
                    </div>
                    <nav class="nav-menu">
                        <a href="./index.html">Home</a>
                        <a href="./catalog.html">Catalog</a>
                        <a href="./shops.html">Shops</a>
                        <a href="./contact.html">Contact</a>
                        <a href="./products.html">Products</a>
                    </nav>
                </div>
            </header>
            <section>
                <div class="container-box">
                    <div class="box-buying">
                        <h2>Buy a product</h2>
                        <h3>List of products</h3>
                        <div class="block-table">
                            <table class="buying-table">
                                <tbody>
                                    <tr>
                                        <th>ID</th>
                                        <th>Name</th>
                                        <th>Mark</th>
                                        <th>Sizes</th>
                                        <th>Colors</th>
                                        <th>Price</th>
                                        <th>Discount</th>
                                    </tr>
                                    '''

        #Calls the function that queries to the database to get all the data from each document in 'bikes' collection.
        for document in get_all_data_from_accessories()['documents']:

            #Saves each value in a variable.
            idProduct = document['_id']
            nameProduct = document['name']
            markProduct = document['mark']
            priceProduct = document['price']
            
            discountProduct = document['discount']
            if discountProduct is False:
                discountProduct = "No discount"
            else:
                discountProduct = f"{discountProduct}%"

            try:
                colorProduct = ', '.join(str(color) for color in document['description']['color'])
            except KeyError:
                color = None

            try:
                sizeProduct = ', '.join(str(size) for size in document['description']['size'])
            except KeyError:
                size = None

            #This will add the following html code to the variable 'html', creating a new row in the table in booking.html
            #with the specified bike's information.
            #Because is in a for loop, it will create a row for each bike.
            html += f'''<tr>
                                        <td>{idProduct}</td>
                                        <td>{nameProduct.title()}</td>
                                        <td>{markProduct.title()}</td>
                                        <td>{sizeProduct}</td>
                                        <td>{colorProduct.title()}</td>
                                        <td>{priceProduct}€</td>
                                        <td>{discountProduct}</td>
                                    </tr>
                                    '''

        html += '''</tbody>
                            </table>
                        </div>
                        <h3>Buying formulary</h3>
                        <form action="#" method="get">
                            <div class="form-item">
                                <label for="name_surname">Full name:</label>
                                <input type="text" id="name_surname" name="name_surname" placeholder="Write your full name." required>
                            </div>
                            <div class="form-item">
                                <label for="dni_nie">DNI/NIE:</label>
                                <input type="text" id="dni_nie" name="dni_nie" placeholder="Write your DNI/NIE." required>
                            </div>
                            <div class="form-item">
                                <label for="product_id">Select a product:</label>
                                <select id="product_id" name="product_id" required>
                                    <option value="">Choose the product's ID</option>
                                    '''
        for document in get_all_data_from_accessories()['documents']:

            #Saves each value in a variable.
            idProduct = document['_id']

            #This will add the following html code to the variable 'html', creating a option to select in the form in buy-product.html
            #with the product's ID.
            #Because is in a for loop, it will create a option to select for each product.
            html += f'''<option value="{idProduct}">{idProduct}</option>
                                    '''

        html += '''</select>
                            </div>
                            <div class="form-item">
                                <label for="details">Details:</label>
                                <br>
                                <textarea id="details" name="details" rows="10" cols="41" maxlength="200" placeholder="Write your wanted color and size." required></textarea>
                            </div>
                            <br>
                            <div class="form-item-button">
                                <input type="submit" class="button" value="Send">
                                <input type="reset" class="button" value="Reset">
                            </div>
                        </form>
                    </div>
                </div>
            </section>
                
            <footer>
                <div class="container-footer">
                    <p id="copyright">Copyright &#169; 2022</p>
                </div>
            </footer>
        </div>
    </body>
</html>
'''

        #Writes the content of the variable 'html' in the file created previously (buy-products.html), and then closes the file.
        file.write(html)
        file.close()

    except FileNotFoundError:

        #If the file doesn't exit, it will create it.
        #But if the directory doesn't exist, it will return a FileNotFoundError.
        #With this try/except block, it will return the following message in case of a FileNotFoundError:
        print("Directory not found.")

if __name__ == '__main__':

    create_buy_product()
