#To succesfuslly invoke the function 'get_all_data_from_companies', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_companies import get_all_data_from_companies
from crud_db.find.count_bikes_by_mark import count_bikes_by_mark
from pathlib import Path
from os import getcwd as getCurrentDirectory


def create_shops():
    
    try:
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
            <meta name="author" content="Samuel_Piedra and Noa_Cocaña">
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
            <div class="index-footer">
                <header>
                    <div class="container-header">
                        <div class="container-header-logo">
                            <img src="./img/logo-webpage.png" height="65px" width="90px" alt="rental logo">  
                        </div>
                        <nav class="nav-menu">
                            <a href="./index.html">Home</a>
                            <a href="./catalog.html">Catalog</a>
                            <a href="./products.html">Products</a>
                            <a href="./shops.html">Shops</a>
                            <a href="./contact.html">Contact</a>
                        </nav>
                    </div>
                </header>
                <section>
                <div class="container-box">
                """
    
        count = 0
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
            google_map = document['address']['google_map']
            
            nameMark = count_bikes_by_mark()['documents'][count]['_id'].replace(' ', '-')
            
            html += f'''<div class="box-shops">
                        <i class="fa fa-map-marker" id="icon-shop"></i>
                        <h2>{name}</h2>
                        <div class="box-shops-information">
                            <div class="box-shops-information-items">
                                <h3>Address</h3>
                                <p>{district}, {street}, {zip_code}</p>
                                <p>{city}, {autonomous_community}, {country_code}</p>
                            </div>
                            <div class="box-shops-information-items">
                                <h3>Contact information</h3>
                                <p><b>Email:</b> {email}</p>
                                <p><b>Tel:</b> {phone_number}</p>
                            </div>
                        </div>
                        <iframe src="{google_map}" class="google-map" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-whe
                        n-downgrade"></iframe>
                        <div class="box-shops-button"><a href="./catalog-bikes-{nameMark.lower()}.html" class="container-button">See bikes</a></div>
                    </div>
                    '''
        
            count += 1
             
    
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

    except FileNotFoundError:

        #If the file doesn't exit, it will create it.
        #But if the directory doesn't exist, it will return a FileNotFoundError.
        #With this try/except block, it will return the following message in case of a FileNotFoundError:
        print("Directory not found.")

if __name__ == '__main__':

    create_shops()
