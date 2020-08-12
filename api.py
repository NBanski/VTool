import os
path = os.getcwd() + "\env\\api.env"

def load_api():
    try:
        i = open(path, 'r').readline().split('=')[1].strip("'")
        return i
    finally:
        print("check")

load_api()