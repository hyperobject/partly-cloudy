"""
Special thanks to @manitou48 and @jasonkuhrt for their help and support
"""


import requests
import re

class Bit:
    def __init__(self, auth_token, device_id):
        self.token = auth_token
        self.id = device_id
        self.headers = {"Authorization": "Bearer " + self.token, "Accept": "application/vnd.littlebits.v2+json"}

    def output(self, pct, dur):
        r = requests.post("https://api-http.littlebitscloud.cc/devices/" + self.id + "/output", data={"percent": pct, "duration_ms": dur}, headers=self.headers)
        return r.text

    def iter_input(self):
        #Use this for raw streaming input
        r = requests.get("https://api-http.littlebitscloud.cc/devices/" + self.id + "/input", headers=self.headers, stream=True)
        for line in r.iter_lines():
            #if line: print line
            yield line   # just fetch one line
        return
    def input(self):
        return int(re.match(".*percent.:(\d+)",self.iter_input().next()).group(1))
