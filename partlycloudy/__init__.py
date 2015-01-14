"""
Special thanks to @manitou48 and @jasonkuhrt for their help and support
"""


import requests
import re
import json

class Bit:
    def __init__(self, auth_token, device_id):
        self.token = auth_token
        self.id = device_id
        self.headers = {"Authorization": "Bearer " + self.token, "Accept": "application/vnd.littlebits.v2+json"}

    def output(self, pct, dur):
        r = requests.post("https://api-http.littlebitscloud.cc/devices/" + self.id + "/output", data={"percent": pct, "duration_ms": dur}, headers=self.headers)
        return r.text

    def raw_stream(self):
        #Use this for raw streaming input
        for line in requests.get("https://api-http.littlebitscloud.cc/devices/" + self.id + "/input", headers=self.headers, stream=True).iter_lines():
            if line:
                yield json.loads(line)

    def stream(self):
        #Use this for raw streaming input
        for line in requests.get("https://api-http.littlebitscloud.cc/devices/" + self.id + "/input", headers=self.headers, stream=True).iter_lines():
            if line:
                yield int(json.loads(line)["payload"]["percent"])

    def input(self):
        return self.stream().next()
