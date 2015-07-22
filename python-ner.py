#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import urllib
from telnetlib import Telnet


TCP_IP = '127.0.0.1'
TCP_PORT = 1234
BUFFER_SIZE = 10024

url = "http://resolver.kb.nl/resolve?urn=ddd:010041671:mpeg21:a0005:ocr"
MESSAGE = urllib.urlopen(url).read().replace('\n','').replace('\r','') +  "\n"
tn = Telnet(TCP_IP, TCP_PORT)
tn.write(MESSAGE)
data = tn.read_all()

for line in data.split():
    if not line.split('/')[1] == "O" and not line.find('MISC') > -1:
        print line
