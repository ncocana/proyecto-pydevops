# Proyecto PyDevops

**Table of contents**

-   [**Proyecto PyDevops**](#proyecto-pydevops)
-   [**Introduction**](#introduction)
-   [**Development**](#development)
-   [**Technical description**](#technical-description)
    -   [**Project architecture**](#project-architecture)
    -   [**Diagram of components**](#diagram-of-components)
    -   [**Diagram E/R**](#diagram-er)
-   [**Development methodology used**](#development-methodology-used)
    -   [**How we applied OCP**](#how-we-applied-ocp)
    -   [**How we applied SRP**](#how-we-applied-srp)
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

# Technical description

### Project architecture

* Our website is distributed in five main pages,each page is inside one small oval,the ovals with a bigger size are a short description of the content which changes depending on the oval you are reading at the moment. As you can see there are four pages with a rectangle below them,these rectangles are actions that the user can
do.
* The rectangles mentioned before are linked into one rectangle with a Python logo, this is because all the structure and elements involved in the diagram were  constructed by this programm.
* The databases rectangle refers to how we stored the data in the database (arrays,strings,integers...etc),which determinates the distribution of the code wrote in the Python files and also into the structure of the the final product.

![arquitecture](https://user-images.githubusercontent.com/114516225/206882958-be10ffd3-e9b4-4a1e-aa88-f55d1f31a58e.png)

### Diagram of components

The diagram allows us to visualize the organization of the components and the dependency relationships between them. 
* The dependencies are in decreasing order e.g; We can't run our website called Rental Bikes if we have some issues with Github pages soo this create a dependency.
* Github Pages only wroks if it's linked to HTML files.HTML depends on the Python code wrote to create them.
* If we don't configure well or we fail writing the queries to make an instance using the CRUD functions, Python returns an error,soo we haven't data to implement into a Python file and then transform it to HTML.
* The CRUD functions can work only if we have created a databases before and also we have acces to their collections through a Data API Key.

![components (2)](https://user-images.githubusercontent.com/114516225/206883546-cbb84384-bf86-47c2-a785-882c9b9b8d3e.jpg)

### Diagram E/R

This diagram explains and give sense to the way we stored the data and how we combine them to make the website funtional and optimized for our users and his fullfill possibles demands.

![diagramer](https://user-images.githubusercontent.com/114516225/206885133-6b1f2e30-896e-4068-ba61-8772a7a4afa3.png)

# Development methodology used

We decided in pair the aspect and the distribution of our web,making a research and collecting ideas from real pages. Our first ideas were about the main page and we drawn it in paper during one class but we didn't reach an agreement. But we had an idea in common that was design an easy webpage model.

One of us watched a tutorial and create a navegation bar and deliver a idea that was accepted from both fellows,from this point we continue working and we implement our own style to our website. In every step to built our page we put on practise the Open Closed Principle (OCP) and Single Responsabilty Principle(SRP)
We divided the project in order that both of us touch the differents subjects involved in this project like programming,markup languages,informatic systems and databases subject.

### How we applied OCP

When we write the CRUD operations we know that for extract the data we used a similar structure of code that mustn't be changed,if we do it we can't connect to our cluster.Soo this part it's closed to modification.

To extract data we modified and extend the code to write queries for obtain different data from mixed fields,as much as we want.This part is open to extension because we can write and used differents logical operators or make it simple with basic operators.

Other example can be our design pages once we decided the structure we didn't modified it.But passing the days we extend the content adding form,interactive buttoms,videos.

### How we applied SRP

Both of us take the responsability of the code we wrote and we worked in separated branches.Once a task was finished the other mate checks the code trying to detect mistakes and with the objective of optimized the code and make the responsable fix the errors or rewrite the code.

### CI/CD

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
