import mysql.connector as sql


DB_NAME = "covid_eda_db"


class MySqlDb:
    """
    A class used to create a MySQL Database.
    """

    def __init__(self, config: dict):
        """Initialize the values"""
        # create connection using config
        self.conn = sql.connect(**config)
        # create cursor object
        self.my_cursor = self.conn.cursor()

    def create_db(self, DB_NAME):
        """Create a MySQL DB"""
        sql_query = f"CREATE SCHEMA IF NOT EXISTS {DB_NAME}"
        self.my_cursor.execute(sql_query)
        print(f"DB: {DB_NAME} was created \n")

    def create_table(self, table_name, sql_query):
        """Add a table to the DB"""
        # select DB
        self.my_cursor.execute(f""" USE {DB_NAME} """)
        # execute the query
        self.my_cursor.execute(sql_query)
        print(f"Table: {table_name} was created \n")

    def show_tables(self):
        # show the tables
        self.my_cursor.execute("SHOW TABLES")
        # display tables
        print("Table names:")
        for table in self.my_cursor:
            print(f"{table} \n")

    def insert_into_table(self, table_name, sql_query, values):
        """Insert values into a table"""
        # add all the rows to the db
        self.my_cursor.executemany(sql_query, values)
        # commit the changes
        self.conn.commit()
        print(f"Values inserted into {table_name} \n")

    def select_records(self, sql_query):
        """Select records from a table"""
        self.my_cursor.execute(sql_query)
        # display records
        for x in self.my_cursor:
            print(f"{x} \n")

    def close_conn(self):
        """Close the connection to the DB"""
        self.conn.close()
        print(f"Connection to {DB_NAME} has been closed!")
