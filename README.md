# Proyecto PyDevops

**Table of contents**

-   [**Proyecto PyDevops**](#proyecto-pydevops)
-   [**Introduction**](#introduction)
-   [**Development**](#development)
    -   [**CI/CD**](#cicd)
-   [**Time spent on the project**](#time-spent-on-the-project)
    -   [**Clockify**](#clockify)

# Introduction

This is a project of the first evaluation in the first year in Web application development.  
The aim of this project is to create a webpage of rental bycicles where local people and tourists can check if there are bycicles to rent in an area. And you will ask: why bycicles?  
Well, this is because the excessive numbers of cars in Palma of Mallorca, Balearic Islands. The idea is to promote the use of bycicles instead of cars.

# Development

For this, we used the following programms in that order to obtain and transform our files to run our website:

![image](https://user-images.githubusercontent.com/114516225/206863975-3b791014-7571-44f3-8c52-8f748cac5128.png)

We created a database using MongoDB Atlas, and then extracted the data stored in it using the Mongo DataAPI and its keys in order to insert them into our webpage using Python. Once this is succesfully done, we programmed a serie of functions in Python to write the HTML for each page of our website and imported them in the "master" Python file, which will execute all the functions, creating the webpage executing only one file. The HTMLs will be created in a folder called "docs", which will already contain all the images and CSS needed by the HTML files.  
At the end, we added test cases and try/except blocks on the files in charge of extracting the data and creating the webpage.

## CI/CD

The principles of continuos delivery and continuos integration along all the project are implemented in the following way:
* Run unitary tests cases
* Verifying the code integrity (that it can be compile, that there are no errors, etc).
* Apply the appropriate settings. If we upload the code to a test repository, it goes to a test environment with its configurations.
* To warn of past changes or errors found.

# Time spent on the project

## Clockify

In order to record the time we spent developing the project and see in which parts we spent more time working, we have used the page called [Clockify](https://clockify.me/) to carry out a control of the time spent on the development of the project.

-   **GitHub/Git:** Investigate how Git, GitHub, and GitFlow work.
-   **HTML/CSS:** Design and create the webpage using HTML and CSS.
-   **Data API:** Use the DataAPI of MongoDB to extract the data needed for the webpage, as well as create CRUD functions to read, update, and delete data from the database.
-   **Create HTML with Python:** Using the HTML created previously, develop the Python functions to create the HTML files with the data from the database.
-   **Test Cases:** Add test cases (that can be executed with Pytest and Coverage) and try/except blocks to ensure the application works as intended.
-   **JSON (Discarded):** This was our first take on how to extract the data from MongoDB using the "mongoexport" command to extract the data in JSONs from a Python file and create a function to parse through them and extract the data at will. But unfortunately, the function to parse through the JSONs didn't work as intended, which is why we ended up using the DataAPI from MongoDB to extract the data instead.

![clockify](https://user-images.githubusercontent.com/117761602/206876998-ff386f17-6937-499a-aad1-fbd5e5766f24.jpg)
