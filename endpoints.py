import requests
import json
from datetime import datetime
from api import API_KEY
from log import (log_url_report, log_url_scan)

# To do - make input a list. Also: test variables.
url = "www.google.com"
id = 0

# Single URL request to VT database.
def single_url_scan(m_url):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    params = {"apikey": API_KEY, "url": m_url}
    response = requests.post(url, data=params)
    return response.json()

# Single URL request for site scan.
def single_url_report(id):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    params = {"apikey": API_KEY, "resource" : id}
    response = requests.post(url, params)
    return response.json()
 
print(API_KEY)

# Parse data from make_scan_request(m_url).

# Multiple requests with logging.
def url_scan(arr):
    for _ in arr:
        data = single_url_scan(_)
        filename = datetime.now().strftime("%Y%m%d %H%M%S%f")
        with open(log_url_scan + "\\" + filename + ".json", "w") as f:
            json.dump(data, f)

def url_report(arr):
    for _ in arr:
        data = single_url_report(_)
        print(data)
        filename = datetime.now().strftime("%Y%m%d %H%M%S%f")
        with open(log_url_report + filename + ".json", "w") as f:
            json.dump(data, f)


url_report(["https://www.google.pl", "https://gazeta.pl"])