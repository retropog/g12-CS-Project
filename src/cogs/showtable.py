import mysql.connector
import os
import dotenv
from prettytable import PrettyTable

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


def show_table():
    """
    Shows the entire table and the data within it

    :return:
    table::str
        The table and its data
    error::str
        The error when occured
    """
    if not table_exist():
        return print(f"Table {name} does not exist")
    table = PrettyTable(["ID", "Name", "Class & Section", "Student/Teacher", "Vaccine Dose 1", "Vaccine Dose 2", "Vaccine 1 Date", "Vaccine 2 Date"])
    cursor.execute(f"SELECT * FROM {name}")
    res = cursor.fetchall()

    for row in res:
        table.add_row(list(row))
        # print(list(row))

    print(table)
