import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch")
#r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')
# Convert the BeautifulSoup object to a string
soup_str = str(soup)

import re

# Define the regular expression pattern
pattern = r'\\"regularMarketPrice\\"\s*:\s*(\d+(\.\d+)?)'

# Search the string for the pattern
match = re.search(pattern, soup_str)

# If a match is found, print the matched string
if match:
    print(match.group())
else:
    print("No match found")

