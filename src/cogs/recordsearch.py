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


def record_search():
    if table_exist():
        choice = int(input("Search by? \n1) ID \n2) Name \n3) Class \n[Enter 1, 2 or 3]: "))
        if choice == 1:
            search = int(input("Enter ID of the Person: "))
            try:
                table = PrettyTable(["ID", "Name", "Class & Section", "Student/Teacher", "Vaccine Dose 1", "Vaccine Dose 2", "Vaccine 1 Date", "Vaccine 2 Date"])
                cursor.execute(f"SELECT * FROM {name} WHERE ID = {search}")
                res = cursor.fetchall()
                for row in res:
                    table.add_row(list(row))

                print(table)

            except Exception as e:
                return print(f"No record found for ID {search}")

        elif choice == 2:
            search = str(input("Enter Name of the Person: "))
            try:
                table = PrettyTable(["ID", "Name", "Class & Section", "Student/Teacher", "Vaccine Dose 1", "Vaccine Dose 2", "Vaccine 1 Date", "Vaccine 2 Date"])
                cursor.execute(f"SELECT * FROM {name} WHERE name = '{search}'")
                res = cursor.fetchall()
                for row in res:
                    table.add_row(list(row))

                print(table)

            except Exception as e:
                return print(f"No record found for ID {search}")

        elif choice == 3:
            search = str(input("Enter clsSec of the Person [Class-Section]: "))
            try:
                table = PrettyTable(["ID", "Name", "Class & Section", "Student/Teacher", "Vaccine Dose 1", "Vaccine Dose 2", "Vaccine 1 Date", "Vaccine 2 Date"])
                cursor.execute(f"SELECT * FROM {name} WHERE clsSec = '{search}'")
                res = cursor.fetchall()
                for row in res:
                    table.add_row(list(row))

                print(table)

            except Exception as e:
                return print(f"No record found for ID {search}")

        else:
            return print(f"That is not a valid option")

    else:
        return print(f"Table '{name}' does not exist")
