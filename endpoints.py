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
    # Do usunięcia w wersji finalnej.
    print("Response acquired from server:\n", response.json())
    return response.json()