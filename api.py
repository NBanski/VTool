import os
path = os.getcwd() + "\VTool\environ\\api.env"

# def load_file():

def load_api():
    i = open(path, 'r').read()
    print(i)

# def set_api():

load_api()