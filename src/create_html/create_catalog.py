#To succesfuslly invoke the function 'get_all_data_from_accessories', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_bikes import get_all_data_from_bikes
from pathlib import Path
from os import getcwd as getCurrentDirectory

def create_catalog():

    try:
        #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/catalog.html'.
        working_directory = Path(getCurrentDirectory())
        path = working_directory / "docs" / "catalog.html"

        #Opens the file with the purpose to write on it.
        file = path.open('w', encoding="utf-8")

        #Saves the html content into the variable 'html'.
        html = '''<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Rental Bike - Catalog</title>
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
            <link rel="stylesheet" href="./css/styles-catalog.css">
            <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
            <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
            <base target="_self">
        </head>
        <body id="background-catalog">
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
                '''

        #Calls the function that queries to the database to get all the data from each document in 'bikes' collection.
        for document in get_all_data_from_bikes()['documents']:

            #Saves each value in a variable.
            typeBike = document['type']
            markBike = document['mark']
            minAge = document['characteristics']['min_age']

            isForKids = document['characteristics']['for_kids?']
            if isForKids is True:
                isForKids = 'Yes'
            if isForKids is False:
                isForKids = 'No'
            
            capacitykBike = document['characteristics']['bike_capacity']
            speedsBike = document['characteristics']['number_of_speeds']
            
            #If it is an array, it will unite it in one single string seperated by comas.
            colorsBike = ', '.join(str(color) for color in document['characteristics']['color_bike'])

            #If it is an electric bike, it will get the data from its characteristics as an electric bike. Else, it will not.
            isEBike = document['characteristics']['electric_bike?']
            if isEBike is True:
                isEBike = 'Yes'
                speedEBike = document['characteristics']['characteristics_electric_bike']['speed']
                batteryEBike = document['characteristics']['characteristics_electric_bike']['battery_duration_per_km']
                materialBatteryEBike = document['characteristics']['characteristics_electric_bike']['material_of_battery']
            if isEBike is False:
                isEBike = 'No'

            squaresSizeBike = ', '.join(str(size) for size in document['characteristics']['maker_information']['size of square'])
            materialBike = document['characteristics']['maker_information']['material_of_bike']
            developmentBike = document['characteristics']['maker_information']['development']
            makerBike = document['characteristics']['maker_information']['maker']

            accessoriesBike = ', '.join(str(accessory) for accessory in document['characteristics']['acessories'])

            #If the bike is avalaible, the variable value will be 'Yes'. Otherwise, it will be 'No'.
            avalaibilityBike = document['avalaibility']
            if avalaibilityBike is True:
                avalaibilityBike = 'Yes'
            if avalaibilityBike is False:
                avalaibilityBike = 'No'

            stockShop = document['units_in_shop']
            priceRentBike = document['price_of_rent_per_hour']
            priceBrokeBike = document['price_of_broke']

            #This will add the following html code to the variable 'html', creating a box in catalog.html with the bike's information.
            #Because is in a for loop, it will create a box for each bike.
            html += f'''<div class="box-catalog">
                                <div>
                                <i class="fa fa-bicycle"></i>
                                <h3>{typeBike.title()}</h3>

                                <ul class="container-list">
                                    <li class="container-list-item"><h4>Characteristics</h4></li>
                                    <li class="container-list-item"><b>Mark:</b> {markBike}</li>
                                    <li class="container-list-item"><b>Minim age:</b> {minAge}</li>
                                    <li class="container-list-item"><b>For kids?</b> {isForKids}</li>
                                    <li class="container-list-item"><b>People capacity:</b> {capacitykBike}</li>
                                    <li class="container-list-item"><b>Number of speeds:</b> {speedsBike}</li>
                                    <li class="container-list-item"><b>Colors avalaibles:</b> {colorsBike.title()}</li>
                                    <li class="container-list-item"><b>Accessories:</b> {accessoriesBike.title()}</li>
                                    <li class="container-list-item"><b>Is it electric?:</b> {isEBike}</li>
                                    '''

            #If it an electric bike, it will add the next information. Otherwise, it will not.
            if isEBike == 'Yes':
                html += f'''<li class="container-list-item"><h4>eBike's characteristics</h4></li>
                                    <li class="container-list-item"><b>Speed:</b> {speedEBike}</li>
                                    <li class="container-list-item"><b>Battery duration/km:</b> {batteryEBike}</li>
                                    <li class="container-list-item"><b>Battery's material:</b> {materialBatteryEBike.title()}</li>
                                    '''

            html += f'''<li class="container-list-item"><h4>Maker's information</h4></li>
                                    <li class="container-list-item"><b>Size of squares:</b> {squaresSizeBike}</li>
                                    <li class="container-list-item"><b>Bike's material:</b> {materialBike.title()}</li>
                                    <li class="container-list-item"><b>Development:</b> {developmentBike}</li>
                                    <li class="container-list-item"><b>Maker:</b> {makerBike.title()}</li>
                                    <li class="container-list-item"><h4>Avalaibility</h4></li>
                                    <li class="container-list-item"><b>Is it available?:</b> {avalaibilityBike}</li>
                                    <li class="container-list-item"><b>Stock in shop:</b> {stockShop}</li>
                                    <li class="container-list-item"><h4>Prices</h4></li>
                                    <li class="container-list-item"><b>Rent price:</b> {priceRentBike}€</li>
                                    <li class="container-list-item"><b>Broke price:</b> {priceBrokeBike}€</li>
                                </ul>
                                </div>

                                <div class="box-catalog-button"><a href="./booking-bike.html" class="container-list-button">Book Now!</a></div>
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

        #Writes the content of the variable 'html' in the file created previously (catalog.html), and then closes it.
        file.write(html)
        file.close()

    except FileNotFoundError:

        #If the file doesn't exit, it will create it.
        #But if the directory doesn't exist, it will return a FileNotFoundError.
        #With this try/except block, it will return the following message in case of a FileNotFoundError:
        print("Directory not found.")

if __name__ == '__main__':

    create_catalog()
