import os

path = os.getcwd() + "\\env\\api.env"

# Creates, writes into and reads a single API KEY from a configuration file.
def load_api():
    try:
        with open(path, "r") as f:
            key = f.readline().split('=')[1].strip('"')
        return key
    except FileNotFoundError:
        print("File not found! Creating files...")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write("")
        print("Done.")
        set_api()
    except IndexError:
        print("No valid API Key was found.")
        set_api()

# Writes a single API KEY to a configuration file.
def set_api():
    print("Enter valid VirusTotal API KEY:")
    key = str(input("> "))
    with open(path, "r+") as f:
        f.write("KEY=" + '"' + key + '"')

API_KEY = load_api()