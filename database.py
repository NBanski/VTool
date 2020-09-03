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

def query_scan_id(url_or_id):
    try:
        data = single_url_scan(url_or_id)
        scan_id = data["scan_id"]
        return scan_id
    except KeyError:
        return {"response_code" : "0"}

def extract_report(url_or_id):
    sql_string = "SELECT * FROM reports WHERE url LIKE {} ORDER BY scan_date DESC".format("'%" + url_or_id + "%'")
    try:
        db = get_db()
        report = db.execute(sql_string).fetchone()
        rep_url = report[2]
        rep_positives = report[8]
        rep_all = report[9]
        rep_time = report[4]
        rep_data = rep_url + " - " + rep_positives + "/" + rep_all + " at " + rep_time
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        try:
            sql_string = "SELECT * FROM not_found WHERE resource LIKE {}".format("'%" + url_or_id + "%'")
            print(sql_string)
            not_found = db.execute(sql_string).fetchone()
            url = not_found[1]
            return (url + " not found in the dataset.")
        except TypeError as e:
            print(e)
            return("Incorrect input.")

def extract_report_by_id(url_or_id):
    sql_string = "SELECT * FROM reports WHERE resource LIKE {} ORDER BY scan_date DESC".format("'%" + url_or_id + "%'")
    try:
        db = get_db()
        report = db.execute(sql_string).fetchone()
        rep_url = report[2]
        rep_positives = report[8]
        rep_all = report[9]
        rep_time = report[4]
        rep_data = rep_url + " - " + rep_positives + "/" + rep_all + " at " + rep_time
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        try:
            sql_string = "SELECT * FROM not_found WHERE resource LIKE {}".format("'%" + url_or_id + "%'")
            print(sql_string)
            not_found = db.execute(sql_string).fetchone()
            url = not_found[1]
            return (url + " not found in the dataset.")
        except TypeError as e:
            print(e)
            return("Incorrect input.")

extract_report_by_id("89bf419372266b1d204e494c257ad1717dd3d1af6e18959fe06f6b510023fe98-1599144346")

def sqlite_wildcard(keyword):
    keyword = "'%" + keyword + "%'"
    return keyword

def search_database(url):
    get_tables = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
    tables = get_db().execute(get_tables).fetchall()
    tables_list = []
    for tup in tables:
        for _ in tup:
            tables_list.append(_)
    all_results = []
    for _ in tables_list:
        if _ == "reports":
            sql_string = "SELECT * FROM " + _ + " WHERE url LIKE " + sqlite_wildcard(url)
            results = get_db().execute(sql_string).fetchall()
            for tup in results:
                report_url = tup[2]
                report_result = tup[8] + "/" + tup[9]
                report_date = tup[4]
                res_data = report_url + " " + report_result + " " + report_date
                all_results.append(res_data)
        if _ == "not_found":
            sql_string = "SELECT * FROM " + _ + " WHERE resource LIKE " + sqlite_wildcard(url)
            results = get_db().execute(sql_string).fetchall()
            for tup in results:
                all_results.append(tup[1] + " wasn't found in the dataset.")
    return(all_results)