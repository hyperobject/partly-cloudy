import urllib2 as u
import urllib
import json as j
class Bit:
    def __init__(self, auth_token, device_id):
        self.token = auth_token
        self.id = device_id
        self.headers = {"Authorization": "Bearer " + self.token, "Accept": "application/vnd.littlebits.v2+json"}
    
    def output(self, pct, dur):
        req = u.Request("https://api-http.littlebitscloud.cc/devices/" + self.id + "/output", urllib.urlencode({"percent": pct, "duration_ms": dur}), self.headers)
        return u.urlopen(req).read()
        