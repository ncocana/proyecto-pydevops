# **Proyecto PyDevops**

**Table of contents**

-   [**Proyecto PyDevops**](#proyecto-pydevops)
-   [**Introduction**](#introduction)
-   [**Development**](#development)
    -   [**CI/CD**](#cicd)
-   [**Time comparison**](#time-comparison)
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

# Time comparison

## Clockify
