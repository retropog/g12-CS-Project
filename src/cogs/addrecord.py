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


def add_record():
    """
    Adds a record to the table with specified information

    :return:
    print::str
        Success conformation or error when either occurs
    """
    if not table_exist():
        return print(f"Table '{name}' does not exist")

    required = ['ID', 'name', 'ST', 'vac1', 'vac2']
    optional = ['clsSec', 'vac1date', 'vac2date']

    user_input = {}

    # Required
    # ID
    _input = input("Enter Admission Number/Teacher ID (Required): ")
    user_input['ID'] = int(_input)

    # Name
    _input = input("Enter Name (required): ")
    user_input['name'] = _input

    # Student/Teacher
    _input = input("Are you a student or teacher? (Required) [Enter S/T]: ")
    user_input['ST'] = _input.upper()

    # Vaccine 1
    _input = input("Have you got your first vaccine? (Required) [Yes/No]: ")
    if str(_input).lower() in ['yes', 'true']:
        vac1 = 'True'
    else:
        vac1 = 'False'

    user_input['vac1'] = vac1

    # Vaccine 2
    _input = input("Have you got your second vaccine? (Required) [Yes/No]: ")
    if str(_input).lower() in ['yes', 'true']:
        vac2 = 'True'
    else:
        vac2 = 'False'

    user_input['vac2'] = vac2

    # Optional
    for j in optional:
        if j == 'clsSec':
            comment = '[Class and Section, Format: Class-Section]:'
        if j == 'vac1date':
            comment = '[Date of 1st Vaccination, Format: YYYY-MM-DD]:'
        if j == 'vac2date':
            comment = '[Date of 1st Vaccination, Format: YYYY-MM-DD]:'

        ask = input(f"Do you want to enter {j}? (Yes/No) ")
        if str(ask).lower() in ['yes']:
            _input = input(f"Enter {j} {comment} ")
            user_input[j] = _input

        else:
            pass

    fields = []
    values = []
    for i in user_input:
        fields.append(i)
        values.append(user_input[i])

    f_temp = ', '.join(fields)

    fields = f"({f_temp})"
    values = tuple(values)

    try:
        query = f"INSERT INTO {name} {fields} VALUES {values}"
        cursor.execute(query)
        db.commit()
        print(f"Record added")

    except Exception as e:
        print(f"An error occured: {e}")
