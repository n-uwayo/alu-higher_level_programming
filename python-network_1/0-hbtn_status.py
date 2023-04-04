#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""
#import urllib.request to make HTTP requests
import urllib.request

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    html = response.read()

print("Body response:")
print(f"\t- type: {type(html)}")
print(f"\t- content: {html}")
print(f"\t- utf8 content: {html.decode('utf-8')}")
