#!/usr/bin/python3
"""fetches https://alu-intranet.hbtn.io/status"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        c = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(c)))
        print("\t- content: {}".format(c))
        print("\t- utf8 content: {}".format(c.decode("utf-8"))`)
