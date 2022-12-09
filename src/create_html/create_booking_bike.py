#To succesfuslly invoke the function 'get_all_data_from_accessories', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './src/')
from queries_db.get_all_data_from_bikes import get_all_data_from_bikes
from pathlib import Path
from os import getcwd as getCurrentDirectory

def create_booking_bike():
    
    try:
        #Assigns the desired path to where the html file will create itself. In this case, the html will be in './docs/booking-bike.html'.
        working_directory = Path(getCurrentDirectory())
        path = working_directory / "docs" / "booking-bike.html"

        #Opens the file with the purpose to write on it.
        file = path.open('w', encoding="utf-8")

        #Saves the html content into the variable 'html'.
        html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Rental Bike - Book a Bike</title>
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
        <link rel="stylesheet" href="./css/styles-booking-bike.css">
        <script src="https://kit.fontawesome.com/2cb25f2c39.js" crossorigin="anonymous"></script>
        <link rel="icon" type="image/x-icon" href="./img/favicon.ico">
        <base target="_self">
    </head>
    <body id="background-booking">
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
                    <div class="box-booking">
                        <h2>Book a bike</h2>
                        <h3>List of bikes</h3>
                        <div class="block-table">
                            <table class="booking-table">
                                <tbody>
                                    <tr>
                                        <th>ID</th>
                                        <th>Type</th>
                                        <th>Mark</th>
                                        <th>Is it electric?</th>
                                        <th>Capacity</th>
                                        <th>Availability</th>
                                        <th>Rent price</th>
                                        <th>Broke price</th>
                                    </tr>
                                    '''
                                    
    #Calls the function that queries to the database to get all the data from each document in 'bikes' collection.
    for document in get_all_data_from_bikes()['documents']:

        #Saves each value in a variable.
        idBike = document['_id']
        typeBike = document['type']
        markBike = document['mark']
        capacitykBike = document['characteristics']['bike_capacity']

        #If it is an electric bike, the variable value will change to 'Yes'. Else, it will change to 'No'.
        isEBike = document['characteristics']['electric_bike?']
        if isEBike is True:
            isEBike = 'Yes'
        if isEBike is False:
            isEBike = 'No'

        #If the bike is avalaible, the variable value will be 'Yes'. Otherwise, it will be 'No'.
        avalaibilityBike = document['avalaibility']
        if avalaibilityBike is True:
            avalaibilityBike = 'Yes'
        if avalaibilityBike is False:
            avalaibilityBike = 'No'

        priceRentBike = document['price_of_rent_per_hour']
        priceBrokeBike = document['price_of_broke']

        #This will add the following html code to the variable 'html', creating a new row in the table in booking.html
        #with the specified bike's information.
        #Because is in a for loop, it will create a row for each bike.
        html += f'''<tr>
                                        <td>{idBike}</td>
                                        <td>{typeBike.title()}</td>
                                        <td>{markBike}</td>
                                        <td>{isEBike}</td>
                                        <td>{capacitykBike}</td>
                                        <td>{avalaibilityBike}</td>
                                        <td>{priceRentBike}€</td>
                                        <td>{priceBrokeBike}€</td>
                                    </tr>
                                    '''

        html += '''</tbody>
                            </table>
                        </div>
                        <h3>Booking formulary</h3>
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
                                <label for="bike_id">Select a bike:</label>
                                <select id="bike_id" name="bike_id" required>
                                    <option value="">Choose the bike's ID</option>
                                    '''
                                    
        #Saves each value in a variable.
        idBike = document['_id']
        typeBike = document['type']

        #This will add the following html code to the variable 'html', creating a option to select in the form in booking.html
        #with the ID's bike.
        #Because is in a for loop, it will create a option to select for each bike.
        html += f'''<option value="{idBike}">{idBike} - {typeBike.title()}</option>
                                '''

        html += '''</select>
                            </div>
                            <div class="form-item">
                                <label for="details">Details:</label>
                                <br>
                                <textarea id="details" name="details" rows="10" cols="41" maxlength="200" placeholder="Write your prefered color and size of square." required></textarea>
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

        #Writes the content of the variable 'html' in the file created previously (booking-bike.html), and then closes the file.
        file.write(html)
        file.close()

    except FileNotFoundError:

        #If the file doesn't exit, it will create it.
        #But if the directory doesn't exist, it will return a FileNotFoundError.
        #With this try/except block, it will return the following message in case of a FileNotFoundError:
        print("Directory not found.")

if __name__ == '__main__':

    create_booking_bike()
