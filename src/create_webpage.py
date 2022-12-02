from create_html.create_index import create_index
from create_html.create_catalog import create_catalog

#Function to execute all the files needed to create the webpage.
def create_webpage():

    #Creates the page 'indedx.html'.
    create_index()

    #Creates the page 'catalog.html'.
    create_catalog()

#Execute it in the terminal with "python .\src\create_webpage.py".
create_webpage()
