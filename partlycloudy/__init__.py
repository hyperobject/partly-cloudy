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
        self.headers = {"Authorization": "Bearer " + self.token}

    def output(self, pct, dur):
        r = requests.post("https://api-http.littlebitscloud.cc/v3/devices/" + self.id + "/output", data={"percent": pct, "duration_ms": dur}, headers=self.headers)
        return r.text

    def json_stream(self):
        #Use this for raw streaming input
        for line in requests.get("https://api-http.littlebitscloud.cc/v3/devices/" + self.id + "/input", headers=self.headers, stream=True).iter_lines():
            if line:
                yield json.loads(line[5:])

    def raw_stream(self):
        #Use this for raw streaming input
        for line in requests.get("https://api-http.littlebitscloud.cc/v3/devices/" + self.id + "/input", headers=self.headers, stream=True).iter_lines():
            if line:
                yield line

    def stream(self):
        #Use this for raw streaming input
        for line in requests.get("https://api-http.littlebitscloud.cc/v3/devices/" + self.id + "/input", headers=self.headers, stream=True).iter_lines():
            if line:
                yield int(json.loads(line[5:])["percent"])

    def overclock(self, interval):
    	r = requests.put("https://api-http.littlebitscloud.cc/v3/devices/" + self.id, data={"input_interval_ms":interval}, headers=self.headers)
    	return r.text

    def input(self):
        #print "https://api-http.littlebitscloud.cc/devices/v3/" + self.id + "/input"
        return self.stream().next()

    def url(self):
    	return "https://api-http.littlebitscloud.cc/v3/devices/" + self.id
