import os
import sqlite3

config_path = os.path.join(os.getcwd(), "settings", "settings.conf")
api_path = os.path.join(os.getcwd(), "settings", "api.env")

# Creates, writes into and reads a single API KEY from the api.env file.
def load_api():
    try:
        with open(api_path, "r") as f:
            key = f.readline().split('=')[1].strip('"')
        return key
    except FileNotFoundError:
        print("File not found! Creating files...")
        os.makedirs(os.path.dirname(api_path), exist_ok=True)
        with open(api_path, "w") as f:
            f.write("")
        print("Done.")
        set_api()
    except IndexError:
        print("No valid API Key was found.")
        set_api()

# Writes a single API KEY to the api.env file.
def set_api():
    print("Enter valid VirusTotal API KEY:")
    key = str(input("> "))
    with open(api_path, "r+") as f:
        f.write("KEY=" + '"' + key + '"')

API_KEY = load_api()