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


def delete_record():
    """
    Deletes a record identified by the ID provided

    :return:
    print::str
        Confirmation if record successfully deleted
        Error if an error occures
    """
    if table_exist():
        _id = int(input("Enter ID for person to delete record: "))

        try:
            cursor.execute(f"DELETE FROM {name} WHERE ID='{_id}'")
            db.commit()
            print("Deleted record")

        except:
            return print(f"No record found for ID {_id}")

    else:
        return print(f"Table '{name}' does not exist")
