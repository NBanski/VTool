import requests
import json
from settings import load_api

# Single request to initiate a scan.
def single_url_scan(url_or_id):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    API_KEY = load_api()
    params = {"apikey": API_KEY, "url": url_or_id}
    response = requests.post(url, data=params)
    return response.json()

# Single request to get a report.
def single_url_report(url_or_id):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    API_KEY = load_api()
    params = {"apikey": API_KEY, "resource" : url_or_id}
    response = requests.post(url, params)
    return response.json()
