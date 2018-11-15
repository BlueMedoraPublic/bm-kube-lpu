#!/usr/bin/env python3
import fire
import os
import requests
requests.packages.urllib3.disable_warnings()



def test(host, token, api=6443, kubelet=10250) :
    target = KubeHost(hostname=host, token=token, api_port=api, kubelet_port=kubelet)
    target.test()



class KubeHost:
    def __init__(self, hostname, token, api_port, kubelet_port):
        self.hostname = hostname
        self.api_port = ":" + str(api_port)
        self.kubelet_port = ":" + str(kubelet_port)

        self.headers = {
            "Authorization": "Bearer " + token
        }

        self.endpoints = [
            # api server endpoints
            "https://" + self.hostname + self.api_port + "/version",
            "https://" + self.hostname + self.api_port + "/api/v1/nodes",
            "https://" + self.hostname + self.api_port + "/api/v1/pods",
            "https://" + self.hostname + self.api_port + "/api/v1/namespaces",

            # kubelet endpoints
            "https://" + self.hostname + self.kubelet_port + "/spec",
            "https://" + self.hostname + self.kubelet_port + "/stats/summary"
        ]

    def test(self):
        result = {}
        for endpoint in self.endpoints:
            r = requests.get(endpoint, headers=self.headers, verify=False)
            print(endpoint + ": " + str(r.status_code))


if __name__ == '__main__':
  fire.Fire(test)
