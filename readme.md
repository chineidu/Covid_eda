# Covid19 EDA Project

## Data

The data was obtained from [Our World in Data](https://ourworldindata.org/covid-deaths). It contains Covid 19 data up until 7th June, 2021.

## Data Cleaning

The data was cleaned and transformed using Python.

* The records with missing continent were dropped.
* Null values in numerical columns were replaced with 0.
* Null values in categorical columns with were replace 'NULL'.
* The features in the data were converted to the appropriate data types.

## ETL

Custom Python functions were written which were used to:

* create a MySQL connection using mysql-connector.
* create MySQL database.
* create tables.
* populate the tables.
* select records from the tables.
* close the connection.

## EDA

* EDA was carried out in Jupyter notebook.
* Several EDA queries were also written in MySQL.

## Dashboard

![covid-dashboard](https://i.postimg.cc/rsTyPwxs/covid-dashboard.jpg)

A dashboard was built using Tableau Public which can be found [here](https://public.tableau.com/app/profile/chinedu.ezeofor/viz/Covid19Dashboard_16237024192830/Covid19Dashboard).
