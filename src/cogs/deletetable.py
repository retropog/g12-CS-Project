import mysql.connector
import os
import dotenv

from cogs.tableexist import table_exist

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


def delete_table():
    """
    Deletes the default table with all the data

    :return:
    print::str
        Confirmation if table successfully deleted
    """
    if table_exist():
        confirmation = str(input(f"Are you sure you want to delete '{name}'? (Yes/No) "))

        if confirmation.lower() == 'yes':
            cursor.execute(f"DROP TABLE {name}")
            db.commit()
            return print(f"Table '{name}' was deleted")
        else:
            return print("Table deletion cancelled")
    else:
        return print(f"Table '{name}' does not exist")
