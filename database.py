import os
import sqlite3
from endpoints import (single_url_report, single_url_scan)
from sqlite3 import Error

database_directory = os.path.join(os.getcwd(), "database")
database_path = os.path.join(os.getcwd(), "database", "vtool_database.db")

# Creates database directory.
def create_directory():
    if os.path.isdir(database_directory):
        pass
    else:
        os.makedirs(database_directory)
        
# Creates database and connects to it.
def get_db():
    connection = None
    try:
        create_directory()
        connection = sqlite3.connect(database_path)
    except FileExistsError:
        print("There's already a database with this name.")
    except Error as e:
        print(e)
    return connection

# Create report table.
def init_db():
    db = get_db()
    warning = input("""You are trying to recreate the {} database. 
All current data will be lost!
Continue? (Y\\N)\n> """.format(database_path))
    if warning == "Y":
        with open("schema.sql") as f:
            db.executescript(f.read())
    else:
        print("Database recreation aborted.")

def insert_report(url_or_id):
    # Here we're taking data from singe_url_report(with args) and mold it into partial SQL command.
    data = single_url_report(url_or_id)
    columns = list(data.keys())[:10]
    table_name = "reports"
    sql_string = 'INSERT INTO {} '.format(table_name)
    sql_string += "(" + ", ".join(columns) + ")\nVALUES " + "("

    # Here we're exctracting key values from JSON data to join it with previous command.
    values = list(data.values())[:10]
    for _ in values:
        sql_string += "'" + str(_) + "'" + ", "
    sql_string = sql_string[:-2] + ")"
    print(sql_string)
    try:
        db = get_db()
        db.executescript(sql_string)
    except sqlite3.IntegrityError as e:
        print(e)