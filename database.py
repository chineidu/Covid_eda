import os
from utils import table_1, table_2
from config import DB_NAME, MySqlDb


# configuration
config = {
    "host": "localhost",
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PSWD"),
}


def main():
    """Create DB, tables and populate the tables"""
    # instantiate MySqlDb object
    my_db = MySqlDb(config)
    # create DB
    try:
        my_db.create_db(DB_NAME)
    except Exception as e:
        print(e)

    # create table 1
    table_name = "Covid_deaths"
    sql_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}
                        (
                            ISO_code VARCHAR(100),
                            Continent VARCHAR(100),
                            Country VARCHAR(100),
                            Date DATE,
                            Population INT,
                            Total_cases INT,
                            New_cases INT,
                            Total_deaths INT,
                            New_deaths INT                    
                        )
                """
    try:
        my_db.create_table(table_name, sql_query)
    except Exception as e:
        print(e)
    #### Populate table
    table1 = table_1()
    table1_vals = []  # save the data from table1 in a list
    for row in table1.itertuples():
        val = row[1:]
        table1_vals.append(val)
    sql_query = f"""
                    INSERT INTO {table_name}
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    try:
        my_db.insert_into_table(table_name, sql_query, table1_vals)
    except Exception as e:
        print(e)

    # create table 2
    table_name = "Covid_vaccinations"
    sql_query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}
                        (
                            ISO_code VARCHAR(100),	
                            Continent VARCHAR(100),
                            Country VARCHAR(100),
                            Date DATE,
                            New_tests INT,
                            Total_tests	INT,
                            Positive_rate FLOAT,
                            Tests_per_case FLOAT,
                            Tests_units VARCHAR(100),
                            Total_vaccinations INT,
                            People_vaccinated INT,
                            People_fully_vaccinated INT,
                            New_vaccinations INT,
                            Stringency_index FLOAT,	
                            Population_density FLOAT,
                            Median_age FLOAT,
                            Aged_65_older FLOAT,
                            Aged_70_older FLOAT,	
                            GDP_per_capita FLOAT,					
                            Handwashing_facilities FLOAT,
                            Hospital_beds_per_thousand FLOAT,
                            Life_expectancy FLOAT,
                            Human_development_index FLOAT                  
                        )
                """
    try:
        my_db.create_table(table_name, sql_query)
    except Exception as e:
        print(e)

    ### Populate table
    table2 = table_2()
    table2_vals = []  # save the data from table1 in a list
    for row in table2.itertuples():
        val = row[1:]
        table2_vals.append(val)
    sql_query = f"""
                    INSERT INTO {table_name}
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    try:
        my_db.insert_into_table(table_name, sql_query, table2_vals)
    except Exception as e:
        print(e)

    # show tables
    my_db.show_tables()
    # select records
    table_name = "Covid_deaths"
    sql_query = f"SELECT * FROM {table_name} LIMIT 5"
    try:
        my_db.select_records(sql_query)
    except Exception as e:
        print(e)
    # select records
    table_name = "Covid_vaccinations"
    sql_query = f"SELECT * FROM {table_name} LIMIT 5"
    try:
        my_db.select_records(sql_query)
    except Exception as e:
        print(e)
    # close the connection
    my_db.close_conn()


if __name__ == "__main__":
    main()
