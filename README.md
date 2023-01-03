# Proyecto PyDevops

**Table of contents**

-   [**Introduction**](#introduction)
-   [**Manual**](#manual)
    -   [**Pre-requirements**](#pre-requirements)
    -   [**Instalation on Windows**](#instalation-on-windows)
    -   [**Use**](#use)
-   [**Technical description**](#technical-description)
    -   [**Project architecture**](#project-architecture)
    -   [**Diagram of components**](#diagram-of-components)
-   [**Development methodology used**](#development-methodology-used)
    -   [**How we applied OCP**](#how-we-applied-ocp)
    -   [**How we applied SRP**](#how-we-applied-srp)
    -   [**CI/CD**](#cicd)
-   [**Time spent on the project**](#time-spent-on-the-project)
    -   [**Clockify**](#clockify)
-   [**Conclusions**](#conclusions)
    -   [**Possible improvements**](#possible-improvements)
    -   [**Difficulties found**](#difficulties-found)

# Introduction

The excessive number of cars on the roads of the Balearic Islands has become a problem, especially in the high tourist season and in certain areas. To try to alleviate this situation, the Government of the Balearic Islands is considering various measures, including promoting the use of rental bicycles instead of rental cars.  

The idea is to create a platform where local people and tourists can check the availability of rental bikes in an area. It is about building an aggregator where companies could use their fleet of bicycles.

As students of the first year of the Higher Degree in Web Application Development, our project consists in creating a no-relational database using MongoDB and extracting the data with the purporse of inserting it on the webpage we will create using a Python. This Python program creates the HTML of the webpage while inserting the data of the database on them. This HTML will be automatically created on a folder called "docs" with all the other files needed for the webpage to properly display (CSS, images, videos, etc). Finally, the remote repository will automatically be pushed to GitHub so the webpage can be deployed through GitHub Pages (this is why the files of the webpage need to be on a folder called "docs", so Pages can properly show the webpage).

# Manual

## Pre-requirements

-   `Git`
-   `Python`
-   `pip3`
-   `requests`
-   `pathlib`

## Instalation on Windows

First, open the terminal and clone the repository with the following command. Before doing this, make sure you're on the directory (folder) were you want to install this repository.

```
git clone https://github.com/ncocana/proyecto-pydevops.git
```

Create a virtual environment to install the dependecies needed. In this case, we will call the virtual environment as ".venv".

```
python -m venv .venv
```

Activate the virtual environment. Depending on what terminal you're on, you will need to execute the required file. For Windows Powershell it will be the one with extension ".ps1", for the CMD it will be ".bat", and for Unix or MacOS it will be called "activate". In this case, we will use the Powershell one:

```
.\.venv\Scripts\Activate.ps1
```

It's possible that when executing this command, you get an error along the lines of "cannot be loaded because the execution of scripts is disabled on this system". If this happens, you will need to open Windows Powershell as administrator and execute the following command. When asked if you're sure, say "yes". This will allow you to execute scripts on your PC, such as the one you need to activate the virtual environment.

```
Set-executionpolicy remotesigned
```

Now you will have to install the requirements with the following command:

```
pip install -r requirements.txt
```

## Use

Create a file called "DataAPIKey.py" and put inside your key to the DataAPI of MongoDB. [Here](https://www.mongodb.com/docs/atlas/api/data-api/) are the instructions of how to generate it.

```
APIKey = "your APIKey"
```

Now, place yourself on the directory of the repository and execute the following command:

```
python .\rental_bikes.py
```

This will start the proccess to extract the data from the database, insert it on the HTML of the webpage, create the HTML files for the webpage, push them to GitHub, and after a while, they will be deployed on GitHub Pages.

You can either view the result locally opening one of the HTML files on the folder "docs", or wait a few minutes until GitHub Pages deploys the webpage to start navegating it.

# Technical description

## Project architecture

* Our website is distributed in five main pages. Each page is inside one small oval (see image); the ovals with a bigger size are a short description of the content which changes depending on the oval you are reading at the moment. As you can see, there are four pages with a rectangle below them, these rectangles are actions that the user can do.
* The rectangles mentioned before are linked into one rectangle with a Python logo. This is because all the structure and elements involved in the diagram were  constructed by this language.
* The databases rectangle refers to how we stored the data in the database (arrays, strings, integers, etc), which determinates the distribution of the code wrote in the Python files and into the structure of the final product.

![arquitecture](https://user-images.githubusercontent.com/114516225/206882958-be10ffd3-e9b4-4a1e-aa88-f55d1f31a58e.png)

## Diagram of components

This component diagram allows us to visualize the organization of the components and the dependency relationships between them. 

![Diagrama de componentes drawio](https://user-images.githubusercontent.com/117761602/210449865-9c5090ff-9648-4be7-b978-a6607146d047.png)

# Development methodology used

We both decided the aspect and the distribution of our web, making a research and collecting ideas from real pages. Our first ideas were about the main page and we drawn it in paper during one class but we didn't reach an agreement. But we had an idea in common which was to design an easy webpage model.

One of us watched a tutorial and created a navegation bar and delivered an idea that was accepted from both fellows; from this point, we continued working and implemented our own style to our website. In every step to build our page, we put on practice the Open Closed Principle (OCP) and Single Responsabilty Principle (SRP).
We divided the project in order so that both of us touched the differents subjects involved in this project such as programming, markup languages, informatic systems, and databases.

We worked in separated branches, one for each feature of the project. Once a task was finished, the other mate checked the code trying to detect mistakes and in order of optimizing the code and make the responsable fix the errors or rewrite the code.

## How we applied OCP

When we wrote the CRUD operations, we knew that for extracting the data we needed to use a similar structure of code and that it shouldn't be changed, otherwise we couldn't connect to our cluster. So this part it's closed to modification.

To extract the data, we modified and extended the code to write queries to obtain different data from mixed fields, as much as we wanted. This part is open to extension because we can write and use differents logical operators or make it simple with basic operators.

Other example can be the design of our webpage; once we decided the structure, we didn't modified it. But passing the days, we extended the content by adding forms, interactive buttons, videos, etc.

## How we applied SRP

We made sure to seperate functions of the src code and test cases into different files so as to better organize the project and promote the use of the Single Responsabilty Principle.

## CI/CD

The principles of continuos delivery and continuos integration along all the project are implemented in the following way:
* Run unitary tests cases.
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

# Conclusions

As result of this project and with the tools that we had at the moment, we designed a responsive web connected with a database.  

The aim of this project is already complete. We implemented all the demands (wrote in the document "Repte Crap -> Craft") we could giving our knowledge at the moment and our limited time.

## Possible improvements

* Looking ahead the next project, we are going to improve our visual content (e.g: adding more images, working more on the interface, and try to add all the features we can between the ones our teachers will tell us).
* Implement the Typer library.

## Difficulties found

We were a bit lost at the beggining on how to extract the required data from MongoDB using Python and parse through it, but we managed to overcome this problem as we advanced on the project and tried several things until we found one that it worked as we wanted.

This project has help us to learn new things that normally would have taken us a longer time to, and we expect to keep learning and improve ourselves in the future.
