from utils import table_1, table_2
from config import create_db, create_table, show_tables, insert_into_table, select_records, close_conn


DB_NAME = 'covid_eda_db'   # Global Variable

def main():
    """Create DB, tables and populate the tables"""
    # create DB
    try:
        create_db(DB_NAME)
    except Exception as e:
        print(e)
        
    # create table 1
    table_name = 'Covid_deaths'
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
        create_table(table_name, sql_query)
    except Exception as e:
        print(e)  
    #### Populate table
    t_1 = table_1()
    t_1_vals = []    # save the data from table1 in a list
    for row in t_1.itertuples():
        val = row[1:]
        t_1_vals.append(val)
    sql_query = f"""
                    INSERT INTO {table_name}
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    try:
        insert_into_table(table_name, sql_query, t_1_vals)
    except Exception as e:
        print(e)


    # create table 2
    table_name = 'Covid_vaccinations'
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
        create_table(table_name, sql_query)
    except Exception as e:
        print(e)
        
    ### Populate table
    t_2 = table_2()
    t_2_vals = []      # save the data from table1 in a list
    for row in t_2.itertuples():
        val = row[1:]
        t_2_vals.append(val)
    sql_query = f"""
                    INSERT INTO {table_name}
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
    try:
        insert_into_table(table_name, sql_query, t_2_vals)
    except Exception as e:
        print(e)




if __name__ == '__main__':
    main()
    # show tables
    show_tables()
    # select records 
    table_name = 'Covid_deaths'
    sql_query = f"SELECT * FROM {table_name} LIMIT 5"
    try:
        select_records(sql_query)
    except Exception as e:
        print(e)       
    # select records
    table_name = 'Covid_vaccinations' 
    sql_query = f"SELECT * FROM {table_name} LIMIT 5"
    try:
        select_records(sql_query)
    except Exception as e:
        print(e)
    # close the connection
    close_conn()
    