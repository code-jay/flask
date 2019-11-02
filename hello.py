import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_gret):
    greeting = 'Hello, {}'.format(who_to_gret)
    return greeting

print(greet('World'))
print(greet('Corey'))
r = requests.get("http://www.google.com")
print(r.status_code)

name = input("Enter your name")
print("Hello, " + name)
