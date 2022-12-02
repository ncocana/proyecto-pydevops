from create_html.create_index import create_index
from create_html.create_catalog import create_catalog
from create_html.create_contact import create_contact

#Function to execute all the files needed to create the webpage.
def create_webpage():

    #Creates the page 'index.html'.
    create_index()

    #Creates the page 'catalog.html'.
    create_catalog()

    #Creates the page 'contact.html'.
    create_contact()

#Execute it in the terminal with "python .\src\create_webpage.py".
create_webpage()
