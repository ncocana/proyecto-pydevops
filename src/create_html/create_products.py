from pathlib import Path
from sys import path as systemPath
from os import getcwd as getCurrentDirectory
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_accessories import get_all_data_from_accessories

def create_products():
    
    #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/index.html'.
    working_directory = Path(getCurrentDirectory())
    path = working_directory / "docs" / "products.html"

    #Opens the file with the purpose to write on it.
    file = path.open('w', encoding="utf-8")


    html = """<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Rental Bike - Products</title>
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
            <link rel="stylesheet" href="./css/styles-products.css">
            <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
            <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
            <base target="_self">
        </head>
        <body id="background-products">
            <div class="index-footer">
                <header>
                    <div class="container-header">
                        <div class="container-header-logo">
                            <img src="./img/logo-webpage.png" height="65px" width="90px" alt="rental logo">  
                        </div>
                        <nav class="nav-menu">
                            <a href="./index.html">Inicio</a>
                            <a href="./catalog.html">Catalog</a>
                            <a href="./shops.html">Shops</a>
                            <a href="./contact.html">Contact</a>
                            <a href="./products.html">Products</a>
                        </nav>
                    </div>
                </header>
                <section>
                    <div class="container-box-products">
                        """
            
    for document in get_all_data_from_accessories()['documents']:

        try:
            features = ', '.join(str(i) for i in document['description']['features'])
        except KeyError:
            features = None

        try:
            material = ', '.join(str(i) for i in document['description']['material'])
        except KeyError:
            material = None

        try:
            color = ', '.join(str(i) for i in document['description']['color'])
        except KeyError:
            color = None

        try:
            size = ', '.join(str(i) for i in document['description']['size'])
        except KeyError:
            size = None

        name = document['name']
        mark = document['mark']
        price = document['price']
        stock = document['on_sale']
        discount = document['discount']
        
        html += f'''<div class="box-products">
                            <i class="fa fa-shopping-bag" id="icon-products"></i>
                            <h2>{name}</h2>
                            <div class="box-products-information">
                                <div class="box-products-information-items">
                                    <h3>Characteristics</h3>
                                    <p><b>Mark</b>: {mark}</p>
                                    '''
        
        if features != None:
            
            html += f'''<p><b>Features</b>: {features}</p>
                                    '''
        
        if material != None:
            
            html += f'''<p><b>Material</b>: {material}</p>
                                    '''
        
        if  color != None:
            
            html += f'''<p><b>Available colors</b>: {color}</p>
                                    '''

        if  size != None:
            
            html += f'''<p><b>Available sizes</b>: {size}</p>
                                '''

        html += f'''</div>
                                <div class="box-products-information-items">
                                    <h3>Price</h3>
                                    <p id=products><b>Price</b>: {price}€</p>
                                    <p><b>Stock</b>: {stock}</p>
                                    '''

        if discount is False:
            html += f'''<p><b>Discount</b>: No discount at the moment</p>
                                '''
        else:

            html += f'''<p><b>Discount</b>: {discount}%</p>
                                '''
        
        html += f'''</div>
                            </div>
                            <div class="box-products-button"><a href="./booking-product.html" class="container-button">Book Now!</a></div>
                        </div>
                        '''
    
    html += '''</div>
                </section>
                <footer>
                    <div class="container-footer">
                        <p id="copyright">Copyright &#169; 2022</p>
                    </div>
                </footer>
            </div>
        </body>
    </html>'''

    file.write(html)
    file.close()
