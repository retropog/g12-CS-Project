import mysql.connector
import os
import dotenv

from cogs.tableexist import table_exist

dotenv.load_dotenv()

# Name of the table to be created
name = os.environ['TABLENAME']

db_vars = {
    'host': os.environ['HOST'],
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'database': os.environ['DATABASE']
}

db = mysql.connector.connect(
    host=db_vars['host'],
    user=db_vars['user'],
    password=db_vars['password'],
    database=db_vars['database']
    )

cursor = db.cursor()


def create_table():
    """
    Creates table with name specified in the .env file

    :return:
    print::str
        Confirmation statement if table was successfully created
        Error if an error occures
    """
    if table_exist():
        print(f"Table '{name}' already exists")
    else:
        try:
            # Create table with fields -> ID, name, clsSec, ST, vac1, vac2, vac1date, vac2date
            cursor.execute(f"CREATE TABLE {name} ( ID INT NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, clsSec VARCHAR(255), ST VARCHAR(1) NOT NULL, vac1 VARCHAR(10) NOT NULL, vac2 VARCHAR(10) NOT NULL, vac1date DATE, vac2date DATE )")
            db.commit()
            print(f"Table '{name}' has been created.")

        except mysql.connector.Error as e:
            print("An error occured: ", e)
