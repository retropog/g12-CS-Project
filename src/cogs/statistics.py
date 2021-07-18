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


def vaccinated_students():
    if not table_exist():
        return print(f"Default table {name} does not exist")

    table = PrettyTable(["ID", "Name"])
    cursor.execute(f"SELECT ID, name FROM {name} WHERE ST = 'S' AND vac2 = 'True'")
    res = cursor.fetchall()

    count = 0

    for i in res:
        table.add_row(list(i))
        count += 1

    print(f"{count} students are fully vaccinated")
    print(table)


def vaccinated_teachers():
    if not table_exist():
        return print(f"Default table {name} does not exist")

    table = PrettyTable(["ID", "Name"])
    cursor.execute(f"SELECT ID, name FROM {name} WHERE ST = 'T' AND vac2 = 'True'")
    res = cursor.fetchall()

    count = 0

    for i in res:
        table.add_row(list(i))
        count += 1

    print(f"{count} students are fully vaccinated")
    print(table)


def vaccine_dose_1_count():
    if not table_exist():
        return print(f"Default table {name} does not exist")

    table = PrettyTable(["ID", "Name"])
    cursor.execute(f"SELECT ID, name FROM {name} WHERE vac1 = 'True'")
    res = cursor.fetchall()

    count = 0

    for i in res:
        count += 1
        table.add_row(list(i))

    cursor.execute(f"SELECT ID, name FROM {name}")
    res = cursor.fetchall()

    total = 0

    for i in res:
        total += 1

    print(f"{count} out of {total} people have got the first dose of vaccine")
    print(table)


def vaccine_dose_2_count():
    if not table_exist():
        return print(f"Default table {name} does not exist")

    table = PrettyTable(["ID", "Name"])
    cursor.execute(f"SELECT ID, name FROM {name} WHERE vac2 = 'True'")
    res = cursor.fetchall()

    count = 0

    for i in res:
        count += 1
        table.add_row(list(i))

    cursor.execute(f"SELECT ID, name FROM {name}")
    res = cursor.fetchall()

    total = 0

    for i in res:
        total += 1

    print(f"{count} out of {total} people have got the second dose of vaccine")
    print(table)


def total():
    if not table_exist():
        return print(f"Default table {name} does not exist")

    count_s = 0
    count_t = 0

    cursor.execute(f"SELECT ST FROM {name}")
    res = cursor.fetchall()

    for i in res:
        if tuple(i)[0] == 'S':
            count_s += 1
        elif tuple(i)[0] == 'T':
            count_t += 1

    total_recorded = count_t + count_s

    print(f"Out of {total_recorded} recorded people, {count_s} are students and {count_t} are teachers")


def stats():
    """
    Show stats for recorded data in the table

    :return:
    table::str
        Menu in tabular form
    """
    table = PrettyTable(["Statistics"])
    table.add_row(["1) Vaccinated Students"])
    table.add_row(["2) Vaccinated Teachers"])
    table.add_row(["3) People with first vaccine"])
    table.add_row(["4) People with second vaccine"])
    table.add_row(["5) Total records"])

    print(table)
    _input = int(input("\nEnter stats module number: "))

    if _input == 1:
        vaccinated_students()
    elif _input == 2:
        vaccinated_teachers()
    elif _input == 3:
        vaccine_dose_1_count()
    elif _input == 4:
        vaccine_dose_2_count()
    elif _input == 5:
        total()
    else:
        return print(f"{_input} is not a valid module number")
