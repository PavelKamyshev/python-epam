import re
import os.path
from collections import Counter
if os.path.exists('access.log'):
    f = open('access.log')
    d = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', f.read())
    f.close()
    for ip in Counter(d).most_common(10):
        print ip[0]
else:
    print("file not found")
