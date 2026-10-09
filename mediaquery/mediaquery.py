#! /usr/bin/python3

import sys
from lib.Argument import Argument
import os
import json

a = Argument(sys.argv)

def print_help():
    print("MediaQuery Command Line,")
    print("Usage: \"mediaquery [-Options...] --file=<filename> --query=<query>\"\n")
    print("Options:")
    print("--Help, -h")


if(a.hasOptionValue('--file')):
    data = json.loads(os.popen('mediainfo --Output=JSON '+a.getOptionValue('--file')).read())
    #json.loads(data) — converts the JSON string into a Python dictionary.
    print(data)
else:
    print_help()