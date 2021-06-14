USE covid_eda_db;
SHOW TABLES;

## Population By Country
SELECT ISO_code,
    Continent,
    Country,
    Population
FROM covid_deaths
GROUP BY Country
ORDER BY Population DESC
LIMIT 300;

## Total_cases vs Total_deaths (Nigeria)
SELECT ISO_code,
    Continent,
    Country,
    Date,
    Population,
    Total_cases,
    Total_deaths
FROM covid_deaths
WHERE Country REGEXP 'Nigeria';

## Probability of dying from Covid
SELECT ISO_code,
    Continent,
    Country,
    Date,
    Population,
    ROUND((Total_deaths * 100) / Total_cases, 2) AS DeathPercentage
FROM covid_deaths
WHERE Country REGEXP 'Nigeria|Canada';

## Total_cases vs Population
SELECT Continent,
    Country,
    Date,
    Total_cases,
    Population,
    ROUND((Total_cases * 100) / Population, 2) AS Total_cases_percentage
FROM covid_deaths
WHERE Country REGEXP 'Nigeria';

## Countries with highest infection rate
SELECT Country,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    ROUND(MAX((Total_cases * 100) / Population), 2) AS Total_cases_percentage
FROM covid_deaths
GROUP BY Country
ORDER BY Total_cases_percentage DESC;

## Countries with highest infection rate plus date
SELECT Country,
    date,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    ROUND(MAX((Total_cases * 100) / Population), 2) AS Total_cases_percentage
FROM covid_deaths
GROUP BY Country,
    date
ORDER BY Total_cases_percentage DESC;

## Countries with highest death rate
SELECT Country,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    ROUND(
        MAX((Total_deaths * 100) / Population),
        2
    ) AS Total_deaths_percentage
FROM covid_deaths
GROUP BY Country
ORDER BY Total_deaths_percentage DESC;

## Countries with highest death 
SELECT Country,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    MAX(Total_deaths) AS Highest_Total_deaths
FROM covid_deaths
GROUP BY Country
ORDER BY Highest_Total_deaths DESC;

## Continents with highest death 
SELECT Continent,
    SUM(Highest_Total_deaths) AS Highest_Total_deaths
FROM (
        SELECT Continent,
            Country,
            MAX(Total_cases) AS Highest_infected_population,
            Population,
            MAX(Total_deaths) AS Highest_Total_deaths
        FROM covid_deaths
        GROUP BY Country
        ORDER BY Highest_Total_deaths DESC
    ) AS Temp
GROUP BY Continent
ORDER BY Highest_Total_deaths DESC;

## Continents with highest death rate 
SELECT Continent,
    AVG(Highest_death_rate) AS Avg_death_rate
FROM (
        SELECT Continent,
            Country,
            MAX(Total_cases) AS Highest_infected_population,
            Population,
            MAX(Total_deaths * 100 / Population) AS Highest_death_rate
        FROM covid_deaths
        GROUP BY Country
        ORDER BY Highest_death_rate DESC
    ) AS Temp
GROUP BY Continent
ORDER BY Highest_death_rate DESC;

## Continents with highest death 
SELECT Continent,
    SUM(Highest_Total_deaths) AS Highest_Total_deaths
FROM (
        SELECT Continent,
            Country,
            MAX(Total_cases) AS Highest_infected_population,
            Population,
            MAX(Total_deaths) AS Highest_Total_deaths
        FROM covid_deaths
        GROUP BY Country
        ORDER BY Highest_Total_deaths DESC
    ) AS Temp
GROUP BY Continent
ORDER BY Highest_Total_deaths DESC;
## Global death rate 
WITH temp AS (
    SELECT Country,
        MAX(Total_deaths) AS Total_deaths,
        MAX(Total_cases) AS Total_cases
    FROM covid_deaths
    GROUP BY 1 # Country
    ORDER BY 2 DESC # Total_deaths
)
SELECT SUM(Total_deaths) AS Total_Deaths,
    SUM(Total_cases) AS Total_Cases,
    ROUND((SUM(Total_deaths) * 100 / SUM(Total_cases)), 2) AS Global_death_rate
FROM temp;

#######################################################################################################################################################################
## Join Covid_Deaths Table and Covid_Vaccinations Table
SELECT *
FROM Covid_Deaths AS cd
    JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
    AND cd.Date = cv.Date
WHERE cd.country REGEXP 'Nigeria'
ORDER BY cv.People_vaccinated DESC;

## Total amount of people in the world that have been vaccinated by country
SELECT *
FROM (
        SELECT cd.Continent,
            cd.Country,
            cd.Population,
            MAX(cv.Total_vaccinations) AS Total_vacc
        FROM Covid_Deaths AS cd
            JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
            AND cd.Date = cv.Date
        GROUP BY cd.Country
        ORDER BY Total_vacc DESC
    ) AS Temp;

## Total amount of people in the world that have been vaccinated
SELECT SUM(Population) AS Total_Population,
    SUM(Total_vacc) AS Total_vaccinations,
    ROUND(SUM(Total_vacc) * 100 / SUM(Population)) AS Total_vacc_percent
FROM (
        SELECT cd.Continent,
            cd.Country,
            cd.Population,
            MAX(cv.Total_vaccinations) AS Total_vacc
        FROM Covid_Deaths AS cd
            JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
            AND cd.Date = cv.Date
        GROUP BY cd.Country
        ORDER BY Total_vacc DESC
    ) AS Temp;

## Vaccinations per day by country
SELECT cd.Continent,
    cd.Country,
    cd.Date,
    cv.New_vaccinations
FROM Covid_Deaths AS cd
    JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
    AND cd.Date = cv.Date
ORDER BY cd.Country,
    cd.Date;
## Vaccinations per day in Nigeria
SELECT cd.Continent,
    cd.Country,
    cd.Date,
    cv.New_vaccinations
FROM Covid_Deaths AS cd
    JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
    AND cd.Date = cv.Date
WHERE cd.country REGEXP 'Nigeria'
ORDER BY cd.Date;

## Cummulative Vaccinations per day in Nigeria
SELECT cd.Continent,
    cd.Country,
    cd.Date,
    cv.New_vaccinations,
    SUM(cv.New_vaccinations) OVER (
        ORDER BY cd.Date,
            Country
    ) AS Cummulative_vaccinations
FROM Covid_Deaths AS cd
    JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
    AND cd.Date = cv.Date
WHERE cd.country REGEXP 'Nigeria'
ORDER BY cd.Date;

# OR Using CTE (Common Table Expressions)
## Cummulative Vaccinations per day in Nigeria
WITH my_table AS (
    SELECT cd.Continent,
        cd.Country,
        cd.Date,
        cv.New_vaccinations
    FROM Covid_Deaths AS cd
        JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
        AND cd.Date = cv.Date
    WHERE cd.country REGEXP 'Nigeria'
    ORDER BY cd.Date
)
SELECT Country,
    Date,
    New_vaccinations,
    SUM(New_vaccinations) OVER (
        ORDER BY Date,
            Country
    ) AS Cummulative_vaccinations
FROM my_table;

## Cummulative Vaccinations per day globally
WITH my_table AS (
    SELECT cd.Continent,
        cd.Country,
        cd.Date,
        cv.New_vaccinations
    FROM Covid_Deaths AS cd
        JOIN Covid_Vaccinations AS cv ON cd.Country = cv.Country
        AND cd.Date = cv.Date
    ORDER BY cd.Date
)
SELECT Country,
    Date,
    New_vaccinations,
    SUM(New_vaccinations) OVER (
        ORDER BY Date,
            Country
    ) AS Cummulative_vaccinations
FROM my_table;

#############################################################################################################################################################
# VIEWS
## Continents with highest death 
CREATE VIEW v_highest_death AS
SELECT Continent,
    SUM(Highest_Total_deaths) AS Highest_Total_deaths
FROM (
        SELECT Continent,
            Country,
            MAX(Total_cases) AS Highest_infected_population,
            Population,
            MAX(Total_deaths) AS Highest_Total_deaths
        FROM covid_deaths
        GROUP BY Country
        ORDER BY Highest_Total_deaths DESC
    ) AS Temp
GROUP BY Continent
ORDER BY Highest_Total_deaths DESC;

## Countries with highest death rate
CREATE VIEW v_countries_highest_death_rate AS
SELECT Country,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    ROUND(
        MAX((Total_deaths * 100) / Population),
        2
    ) AS Total_deaths_percentage
FROM covid_deaths
GROUP BY Country
ORDER BY Total_deaths_percentage DESC;
## Countries with highest infection rate
CREATE VIEW v_countries_highest_infection_rate AS
SELECT Country,
    MAX(Total_cases) AS Highest_infected_population,
    Population,
    ROUND(MAX((Total_cases * 100) / Population), 2) AS Total_cases_percentage
FROM covid_deaths
GROUP BY Country
ORDER BY Total_cases_percentage DESC;
