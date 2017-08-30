import sys
import urllib
import os
import re

dlurl='http://aclweb.org/anthology/L/L14/'
url = urllib.urlopen(dlurl)
tex =[]

for line in url.readlines():
    match=re.search('\[<a href="([A-Z][0-9][0-9].*\.bib)">',line)
    if match:
        tex.append(dlurl + match.group(1))
        
url.close()
print len(tex)

for i in range(len(tex)):
    urllib.urlretrieve(tex[i],'C:\users\shinoda\desktop\\test\\' + os.path.basename(tex[i]))

