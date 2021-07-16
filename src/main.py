# Computer Science project on (Project Name)
# About and aim of the project (Project Aim and About)
#
# Created by:
# Riju Marwah (12-G)
# Sarthak Kumar (12-G)
# Ratul Pal (12-G)
# Session 2021-22 @ Sri Venkateshwar Internation School
#
# External libraries, code and resources used
# 1) MySQL (To access SQL databases)
# 2) DotENV (To access the .env file and import environment variables)
#
# Steps for running the project
# 1) MySQL is a necessity and must be installed on your system
# 2) Enter MySQL host, user, password and database name in the .env file
# 3) (write all imporant steps here)

import os
import mysql.connector
import dotenv

from cogs.create import create_table, table_exist

dotenv.load_dotenv()

# Fetch environment variables from .env file
db_vars = {
    'host': os.environ['HOST'],
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD'],
    'database': os.environ['DATABASE']
}

try:
    # Try connecting to the database
    db = mysql.connector.connect(
        host=db_vars['host'],
        user=db_vars['user'],
        password=db_vars['password'],
        database=db_vars['database']
    )

    # Create a cursor to access the database
    cursor = db.cursor()

    # test
    cursor.execute("DESCRIBE players")
    for x in cursor:
        print(x)

except mysql.connector.Error as e:
    # Return error in case of the same
    print("An error occured: ", e)
