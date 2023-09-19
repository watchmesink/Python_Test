import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
mo = phoneNumRegex.findall('Call me 444-111-5512 and 233-111-1782')
print(mo)