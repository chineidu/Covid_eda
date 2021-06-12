import os
import mysql.connector as sql

# configuration
config = {
    'host': 'localhost',
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PSWD')
}
# create connection using configuration
conn = sql.connect(**config)
# create cursor object
my_cursor = conn.cursor()
DB_NAME = 'covid_eda_db'

# Helper Functions
def create_db(DB_NAME):
    """Create a MySQL DB"""
    sql_query = f"CREATE SCHEMA IF NOT EXISTS {DB_NAME}"
    my_cursor.execute(sql_query)
    print(f"DB: {DB_NAME} was created \n")    

def create_table(table_name, sql_query):
    """Add a table to the DB"""
    # select DB
    my_cursor.execute(f""" USE {DB_NAME} """)
    # execute the query
    my_cursor.execute(sql_query)
    print(f"Table: {table_name} was created \n")    

def show_tables():
    # check for the tables
    my_cursor.execute('SHOW TABLES')
    # display tables
    for table in my_cursor:
        print(table)
        print()    # new line
        
def insert_into_table(table_name, sql_query, values):
    """Insert values into a table"""
    # add all the rows to the db
    my_cursor.executemany(sql_query, values)
    # commit the changes
    conn.commit()
    print(f"Values inserted into {table_name}")
     
def select_records(sql_query):
    """Select records from a table"""
    my_cursor.execute(sql_query)
    # display records
    for x in my_cursor:
        print(f"{x} \n")
        
def close_conn():
    """Close the connection to the DB"""
    conn.close()
    print(f"Connection to {DB_NAME} has been closed!")

