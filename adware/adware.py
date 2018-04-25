#!/usr/bin/env Python

import webbrowser
from time import sleep

site = "http://brasil.campus-party.org/cpbahia/"
verdade = True

while verdade == True:
    sleep(5)
    webbrowser.open(site)
