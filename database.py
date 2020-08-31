import os
import sqlite3
import json
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
        connection = sqlite3.connect(database_path)
    except FileExistsError:
        print("There's already a database with this name.")
    except Error as e:
        print(e)
    return connection

# Create report table.
def init_db():
    create_directory()
    db = get_db()
    with open("schema.sql") as f:
        db.executescript(f.read())

def insert_report(url_or_id):
    # Taking response from HTTP API request.
    data = single_url_report(url_or_id)
    # Here we have to check response code.
    if data["response_code"] == 0:
        table_name = "not_found"
        x = 3
    if data["response_code"] == 1:
        table_name = "reports"
        x = 10

    # Here we're exctracting key values from JSON data to create SQL query.
    columns = list(data.keys())[:x]
    values = list(data.values())[:x]
    sql_string = 'INSERT INTO {} '.format(table_name)
    sql_string += "(" + ", ".join(columns) + ")\nVALUES " + "("
    for _ in values:
        sql_string += "'" + str(_) + "'" + ", "
    sql_string = sql_string[:-2] + ")"
    # Do usunięcia przed wersją finalną.
    print("Query sent to database:\n", sql_string)
    try:
        db = get_db()
        db.executescript(sql_string)
    except sqlite3.IntegrityError as e:
        print(e)

def extract_report(url_or_id):
    sql_string = "SELECT * FROM reports WHERE url LIKE {}".format("'%" + url_or_id + "%'")
    print(sql_string)
    try:
        db = get_db()
        report = list(db.execute(sql_string).fetchone())
        rep_positives = report[8]
        rep_all = report[9]
        rep_time = report[4]
        rep_data = rep_positives + "/" + rep_all + " at " + rep_time
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        print(e)
        return("No report or incorrect input.")