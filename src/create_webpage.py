from create_html.create_index import create_index
from create_html.create_catalog import create_catalog
from create_html.create_contact import create_contact
from create_html.create_booking import create_booking

#Function to execute all the files needed to create the webpage.
def create_webpage():

    #Creates the page 'index.html'.
    create_index()

    #Creates the page 'catalog.html'.
    create_catalog()

    #Creates the page 'contact.html'.
    create_contact()
    
    #Creates the page 'booking.html'.
    create_booking()

#Execute it in the terminal with "python .\src\create_webpage.py".
create_webpage()