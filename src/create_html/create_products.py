from queries_db.get_all_data_from_accessories import get_all_data_from_accessories
from pathlib import Path
from os import getcwd as getCurrentDirectory

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

        nameProduct = document['name']
        markProduct = document['mark']
        priceProduct = document['price']
        stockProduct = document['on_sale']
        discountProduct = document['discount']

        try:
            featuresProduct = ', '.join(str(feature) for feature in document['description']['features'])
        except KeyError:
            featuresProduct = None

        try:
            materialProduct = ', '.join(str(material) for material in document['description']['material'])
        except KeyError:
            materialProduct = None

        try:
            colorProduct = ', '.join(str(color) for color in document['description']['color'])
        except KeyError:
            colorProduct = None

        try:
            sizeProduct = ', '.join(str(size) for size in document['description']['size'])
        except KeyError:
            sizeProduct = None

        
        html += f'''<div class="box-products">
                            <i class="fa fa-shopping-bag" id="icon-products"></i>
                            <h2>{nameProduct}</h2>
                            <div class="box-products-information">
                                <div class="box-products-information-items">
                                    <h3>Characteristics</h3>
                                    <p><b>Mark</b>: {markProduct}</p>
                                    '''
        
        if featuresProduct != None:
            
            html += f'''<p><b>Features</b>: {featuresProduct}</p>
                                    '''
        
        if materialProduct != None:
            
            html += f'''<p><b>Material</b>: {materialProduct}</p>
                                    '''
        
        if  colorProduct != None:
            
            html += f'''<p><b>Available colors</b>: {colorProduct}</p>
                                    '''

        if  sizeProduct != None:
            
            html += f'''<p><b>Available sizes</b>: {sizeProduct}</p>
                                '''

        html += f'''</div>
                                <div class="box-products-information-items">
                                    <h3>Price</h3>
                                    <p id=products><b>Price</b>: {priceProduct}€</p>
                                    <p><b>Stock</b>: {stockProduct}</p>
                                    '''

        if discountProduct is False:
            html += f'''<p><b>Discount</b>: No discount at the moment</p>
                                '''
        else:

            html += f'''<p><b>Discount</b>: {discountProduct}%</p>
                                '''
        
        html += f'''</div>
                            </div>
                            <div class="box-products-button"><a href="./buy-product.html" class="container-button">Buy Now!</a></div>
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
