from pathlib import Path
from os import getcwd as getCurrentDirectory

def create_index():
    
    #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/index.html'.
    working_directory = Path(getCurrentDirectory())
    path = working_directory / "docs" / "index.html"

    #Opens the file with the purpose to write on it.
    file = path.open('w', encoding="utf-8")

    #Saves the html content into the variable 'html'.
    html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Rental Bike - Homepage</title>
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
        <link rel="stylesheet" href="./css/styles-index.css">
        <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
        <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
        <base target="_self">
    </head>
    <body id="background-index">
        <div class="index-footer">
            <div>
                <header>
                    <div class="container-header">
                        <div class="container-header-logo">
                            <img src="./img/logo-webpage.png" height="65px" width="90" alt="rental logo">  
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
                    <div>
                        <h2 id="title-index">Rental Bikes</h2>
                        <p id="p-index"><i><b>the bikes never goes out of style</b></i></p>
                    </div>
                </section>
            </div>
            <footer>
                <div class="container-footer">
                    <p id="copyright">Copyright &#169; 2022</p>
                </div>
            </footer>
        </div>
    </body>
</html>
'''

    #Writes the content of the variable 'html' in the file created previously (index.html), and then closes the file.
    file.write(html)
    file.close()
