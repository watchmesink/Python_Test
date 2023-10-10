# ToDo:
# Create a regex for phone numbers
# create regex for email address
#

import re, urllib.request
page = urllib.request.urlopen('https://adhe.edu/students-parents/arkansas-state-university-system').read()
print(page)