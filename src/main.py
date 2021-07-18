# Computer Science project on School Vaccination Database
# Aim of the project: Python program to store school vaccination data in a MySQL Database

# Created by:
# Riju Marwah (12-G)
# Sarthak Kumar (12-G)
# Ratul Pal (12-G)
# Session 2021-22 @ Sri Venkateshwar Internation School

# External libraries, code and resources used
# 1) MySQL (To access SQL databases)
# 2) DotENV (To access the .env file and import environment variables)
# 3) PrettyTable (To print data in tabular form)

# Steps for running the project
# 1) MySQL is a necessity and must be installed on your system
# 2) Enter MySQL host, user, password and database name in the .env file
# 3) Run this file (main.py)

from cogs.menu import menu


class VaccinationDatabase:
    def __init__(self):
        pass

    @staticmethod
    def run():
        menu()


VaccinationDatabase().run()
