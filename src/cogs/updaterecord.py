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


def update_record():
    """
    Update a specific record. Found using the primary key 'ID'.

    :return:
    print::str
        Success conformation or error when either occurs
    """
    if table_exist():
        _id = int(input("Enter ID of person to update record: "))
        field = str(input("Enter the field you want to update [ID, name, clsSec, ST, vac1, vac2, vac1date or vac2date]: "))
        new_value = str(input("Enter the new value for the field [For Date, Format: YYYY-MM-DD]: "))

        try:
            cursor.execute(f"UPDATE {name} SET {field} = '{new_value}' WHERE ID = {_id}")
            db.commit()
            print("Updated record. Restart may be required to show updated values")

        except mysql.connector.Error as e:
            return print(f"An error occured: {e}")

    else:
        return print(f"Table '{name}' does not exist")
