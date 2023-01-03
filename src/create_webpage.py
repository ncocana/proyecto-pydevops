from create_html.create_index import create_index
from create_html.create_catalog import create_catalog
from create_html.create_booking_bike import create_booking_bike
from create_html.create_products import create_products
from create_html.create_buy_product import create_buy_product
from create_html.create_shops import create_shops
from create_html.create_catalog_btwin import create_catalog_btwin
from create_html.create_catalog_bpro import create_catalog_bpro
from create_html.create_catalog_ducati_corse import create_catalog_ducati_corse
from create_html.create_catalog_balance_toys import create_catalog_balance_toys
from create_html.create_contact import create_contact

#Function to execute all the files needed to create the webpage.
def create_webpage():

    #Creates the page 'index.html'.
    create_index()

    #Creates the page 'catalog.html'.
    create_catalog()
    
    #Creates the page 'booking-bike.html'.
    create_booking_bike()
    
    #Creates the page 'products.html'.
    create_products()
    
    #Creates the page 'buy-product.html'.
    create_buy_product()
    
    #Creates the page 'shops.html'.
    create_shops()
    
    #Creates the page 'catalog-bikes-btwin.html'.
    create_catalog_btwin()
    
    #Creates the page 'catalog-bikes-b-pro.html'.
    create_catalog_bpro()
    
    #Creates the page 'catalog-bikes-ducati-corse.html'.
    create_catalog_ducati_corse()
    
    #Creates the page 'catalog-bikes-balance-toys.html'.
    create_catalog_balance_toys()

    #Creates the page 'contact.html'.
    create_contact()

if __name__ == "__main__":

    #Execute it in the terminal with "python .\src\create_webpage.py".
    create_webpage()
