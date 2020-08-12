import requests
import hashlib
from api import API_PUBLIC

m_url = 'https://www.google.com'

def make_scan_request(m_url):
    url = 'https://www.virustotal.com/vtapi/v2/url/scan'
    params = {'apikey': API_PUBLIC, 'url': m_url}
    response = requests.post(url, data=params)
    print(response.json())

def make_report_request(id):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': API_PUBLIC, 'resource' : id}
    response = requests.post(url, params)
    print(response.json())

# make_request(prep_url)
# make_report_request('d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-1597233114')

print(API_PUBLIC)