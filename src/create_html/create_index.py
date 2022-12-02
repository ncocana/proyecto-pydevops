#To succesfuslly invoke the function 'get_all_data_from_bikes', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from pathlib import Path
from os import getcwd as getCurrentDirectory

def create_index():
    
    #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/index.html'.
    working_directory = Path(getCurrentDirectory())
    path = working_directory / "docs" / "index.html"

    #Opens the file with the purpose to write on it.
    file = path.open('w')

    #Saves the html content into the variable 'html'.
    html = '''<!DOCTYPE html>
<html lang="en">
    <head>
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
        <header>
            <div class="container-header">
                <div class="container-header-logo">
                    <img src="./img/logo-webpage.png" height="65px" width="90px" alt="rental logo">  
                </div>
                <nav class="nav-menu">
                    <a href="./index.html">Inicio</a>
                    <a href="./catalog.html">Catalog</a>
                    <a href="./shops.html">Shops</a>
                    <a href="">Contact</a>
                    <a href="">Products</a>
                </nav>
            </div>
        </header>
        <section>
            <div>
                <h2 id="title-index">Rental Bikes</h2>
                <p id="p-index"><i><b>the bikes never goes out of style</b></i></p>
            </div>
        </section>
        <footer>
            <div class="footer-content">
                <div class="left-box">
                    <div class="upper">
                        <div class="topic">About us</div>
                    <p class="pfooter">Hola</p>
                </div>
                <div class="lower">
                    <div class="topic">Contact</div>
                    <div class="phone">
                        <a href=""><i class="fa fa-phone">97156492</i></a>
                    </div>
                    <div class="email">
                        <a href=""><i class="fa fa-envelope">adcd@gmail.com</i></a>
                    </div>
                </div>
                </div>
                <div class="middle box">
                <div><a href="">1</a></div>
                <div><a href="">2</a></div>
                <div><a href="">3</a></div>
                </div>
                <div class="right-box">
                    <div class="topic">Subscribe</div>
                    <input type="text" placeholder="Enter e-mail address">
                    <input type="submit" name="" value="Send">
                </div>
                <div class="bottom">
                    <p>Copyright &#169; 2022</p>
                </div>
            </div>
        </footer>
    </body>
</html>'''

    #Writes the content of the variable 'html' in the file created previously (index.html), and then closes the file.
    file.write(html)
    file.close()
