import requests
import json
from settings import API_KEY

# To do - make input a list. Also: test variables.
url = "www.google.com"
id = 0

# Single request to initiate a scan.
def single_url_scan(url):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    params = {"apikey": API_KEY, "url": url}
    response = requests.post(url, data=params)
    jsondata = json.dumps(response.json(), indent=4)
    return jsondata

# Single request to get a report.
def single_url_report(url_or_id):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    params = {"apikey": API_KEY, "resource" : url_or_id}
    response = requests.post(url, params)
    # jsondata = json.dumps(response.json(), indent=4)
    return response.json()

# Multiple requests with logging.
# To do: write the function to insert data into PostgreSQL tables.
# Implement it here.

single_url_report("https://www.google.com")