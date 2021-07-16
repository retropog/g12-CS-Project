import mysql.connector
import os
import dotenv

dotenv.load_dotenv()

# Name of the table to be created
name = 'vaccinationtest'

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


def table_exist():
    try:
        cursor.execute("SHOW TABLES")

        tables = []
        for i in cursor:
            # Remove the following characters: (  )  '  ,
            entry = str(i).strip("()',")
            tables.append(entry)

        if name in tables:
            # Return True -> Table already exists
            return True
        else:
            # Return False -> Table does not exist
            return False

    except mysql.connector.Error as e:
        print("An error occured: ", e)


def create_table():
    try:
        # Create table with fields -> ID, name, clsSec, ST, vac1, vac2, vac1date, vac2date
        cursor.execute(f"CREATE TABLE {name} ( ID INT NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, clsSec VARCHAR(255), ST VARCHAR(1) NOT NULL, vac1 VARCHAR(10) NOT NULL, vac2 VARCHAR(10) NOT NULL, vac1date DATE, vac2date DATE )")
        print(f"Table {name} has bee created")

    except mysql.connector.Error as e:
        print("An error occured: ", e)
