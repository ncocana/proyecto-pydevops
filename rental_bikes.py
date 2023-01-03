from src.create_webpage import create_webpage
from src.update_github_pages import updateGitHubPages

def rentalBikes():

    # Creates the webpage.
    create_webpage()

    # Updates the webpage deployed in GitHub Pages.
    updateGitHubPages()

if __name__ == "__main__":

    # Execute it in the terminal with "python .\rental_bikes.py".
    rentalBikes()