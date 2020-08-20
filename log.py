import os
log_url_scan = os.path.join(os.getcwd(), 'logs', 'url scan', "")
log_url_report = os.path.join(os.getcwd(), 'logs', 'url report', "")

# Creates directory for logs.
def create_log_dir():
    try:
        os.makedirs(log_url_scan)
        os.makedirs(log_url_report)
    except FileExistsError:
        print("There's already one one more logs directories.")

create_log_dir()