import requests
import hashlib

my_url = 'https://www.google.com'
r = 'test value'

def prep_request(my_url):
    url_hash = hashlib.sha256(my_url.encode())
    r = url_hash.hexdigest()
    return r

prep_url = prep_request(my_url)

def make_request(prep_url):
    headers = {'x-apikey':'test_value'}
    url = 'https://www.virustotal.com/api/v3/urls'
    r = requests.post(url, headers=headers, data = {'url':prep_url})
    response = r.json()
    return response

make_request(prep_url)