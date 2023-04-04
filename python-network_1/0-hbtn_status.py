#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status.
"""
#import urllib.request to make HTTP requests
import urllib.request

# Use urllib.request.urlopen() to send a GET request to the specified URL
# The response is returned as a response object

with urllib.request.urlopen("https://alu-intranet.hbtn.io/status") as response:
    # Read the contents of the response as bytes and store it in the html variable
    html = response.read()

# Display information about the response using print() statements
print("Body response:")
# Print the type of the html variable (which should be bytes)
print(f"\t- type: {type(html)}")
# Print the raw content of the response (i.e., the bytes)
print(f"\t- content: {html}")
# Print the UTF-8 decoded content of the response (i.e., the text)
print(f"\t- utf8 content: {html.decode('utf-8')}")
