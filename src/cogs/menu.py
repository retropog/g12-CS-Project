import os
import dotenv
from prettytable import PrettyTable

from cogs.addrecord import add_record
from cogs.createtable import create_table
from cogs.deletetable import delete_table
from cogs.deleterecord import delete_record
from cogs.showtable import show_table
from cogs.updaterecord import update_record
from cogs.statistics import stats
from cogs.recordsearch import record_search

dotenv.load_dotenv()

name = os.environ['TABLENAME']


def menu():
    """
    Prints a menu with all usable functions/modules
    :return:
    """

    table = PrettyTable(["Module", "Description"])
    table.add_row(["1) Create Table", "Create table for all vaccination data"])
    table.add_row(["2) Add Record", "Add a new entry to the table"])
    table.add_row(["3) Delete record", "Delete an existing record"])
    table.add_row(["4) Delete Table", "Delete the table and all data"])
    table.add_row(["5) Show Table", "Show all data in the table"])
    table.add_row(["6) Update Record", "Update a field for a record"])
    table.add_row(["7) Statistics", "Show stats for the recorded data"])
    table.add_row(["8) Record Search", "Search records by ID, name or class & section"])
    table.add_row(["9) Exit Menu", "Exit the program"])

    print("\n[ Run (1) when running the program for the first time ]")
    print(table)

    _input = int(input("\nEnter Module Number: "))

    if _input == 1:
        create_table()
        menu()
    if _input == 2:
        add_record()
        menu()
    elif _input == 3:
        delete_record()
        menu()
    elif _input == 4:
        delete_table()
        menu()
    elif _input == 5:
        show_table()
        menu()
    elif _input == 6:
        update_record()
        menu()
    elif _input == 7:
        stats()
        menu()
    elif _input == 8:
        record_search()
        menu()
    elif _input == 9:
        return print("Exiting Menu")
    else:
        print("That is not a valid option")
        menu()
