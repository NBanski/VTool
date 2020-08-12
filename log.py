import os
log_url_scan = os.getcwd() + "\\logs\\url scan\\"
log_url_report = os.getcwd() + "\\logs\\url report\\"

# Creates directory for logs.
def create_log_dir():
    try:
        os.mkdir(log_url_scan)
        os.mkdir(log_url_report)
    except FileExistsError:
        print("There's already one one more logs directories.")