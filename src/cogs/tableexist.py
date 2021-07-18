import mysql.connector
import os
import dotenv

dotenv.load_dotenv()

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


def table_exist():
    """
    Tells if the default table already exists

    :return:
    True::bool
        if table already exists
    False::bool
        if table doesn't exist
    """
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
