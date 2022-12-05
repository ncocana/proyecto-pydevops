from sys import path as systemPath
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_companies import get_all_data_from_companies
from pathlib import Path
from os import getcwd as getCurrentDirectory


def create_shops():
    
    #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/shops.html'.
    working_directory = Path(getCurrentDirectory())
    path = working_directory / "docs" / "shops.html"

    #Opens the file with the purpose to write on it.
    file = path.open('w', encoding="utf-8")


    html = """<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Rental Bike - Products</title>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="author" content="Samuel_Piedra and Noa_Coca�a">
            <meta name="description" content="rent bicycle page">
            <meta name="copyright" content="Samu&Noa">
            <meta name="generator" content="VisualStudioCode">
            <meta name="keywords" content="rent, accesories, shops, bikes, bicycles, type of bicycle">
            <meta http-equiv="content-language" content="text_EN">
            <link rel="stylesheet" href="./css/styles-main.css">
            <link rel="stylesheet" href="./css/styles-shops.css">
            <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
            <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
            <base target="_self">
        </head>
        <body id="background-shops">
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
            """
            
    for document in get_all_data_from_companies()['documents']:
        name = document['name']
        street = document['address']['street_address']
        zip_code = document['address']['zip_code']
        district = document['address']['district']
        city = document['address']['city']
        autonomous_community = document['address']['autonomous_community']
        country_code = document['address']['country_code']
        email = document['contact']['email_address']
        phone_number = document['contact']['phone_number']
        
        
        html += f'''  
        <div class="container-box">
                <div class="box-shops">
                    <i class="fa fa-map-marker" id="icon-shop"></i>
                    <h2 id="h2-shops">{name}</h2>
                    <div class="box-shops-information">
                        <div class="box-shops-information-items">
                            <h2 id="h2-shops2">Address</h2>
                            <p id="companies">{district}, {street}, {zip_code},<br>{city}, {autonomous_community},   {country_code}</p>
                    </div>
                        <div class="box-shops-information-items">
                            <h2 id="h2-shops2">Contact information</h2>
                            <p id=companies><b>Email:</b> {email}<br><b>Tel:</b> {phone_number}</p>
                        </div>
                </div>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3076.3770556218747!2d2.6196049154
                    35978!3d39.551104879475176!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x129792087cbe5111%3A0x
                    fdcc0346ad407921!2sAv.%20de%20Gabriel%20Roca%2C%2054%2C%2007015%20Palma%2C%20Illes%20Balears!5e0!3m2!
                    1sca!2ses!4v1670079910320!5m2!1sca!2ses" width="450" height="300" style="border:0;
                    padding: 20px; border-radius: 10%;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-whe
                    n-downgrade"></iframe>
                </div>
             </div>'''
             
    
    html += '''</section>
            <footer>
                <div class="container-footer">
                    <p id="copyright">Copyright &#169; 2022</p>
                </div>
            </footer>
    </body>
    </html>'''

    file.write(html)
    file.close()
