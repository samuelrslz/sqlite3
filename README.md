# Overview

Simple program to keep track of people I know and the type of relationship that I have with them. The program lets you add new people with their names, age, gender, type of relationship, and country.

[Software Demo Video](https://youtu.be/4fhWivfP56A)

# Relational Database

For this project I'm using SQLite 3 in Python.

The program creates two tables, people and countries.

The people table has the following columns:

- fname TEXT
- lname TEXT
- gender TEXT
- age REAL
- type_of_relation TEXT
- country TEXT

The countries table has the following columns:

- country_name TEXT
- demonym TEXT
- population REAL

A join is performed on people.country = countries.country_name

# Development Environment

- Python 3.9.1
- SQLite 3

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [W3 Schools - SQL Tutorial](https://www.w3schools.com/sql/)
* [Learn SQL in One Hour](https://www.youtube.com/watch?v=9Pzj7Aj25lw&ab_channel=JoeyBlue)

# Future Work

* Implement graphics
* Add more options to edit the countries table