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
    if(a.hasCommand('track') and a.hasOptionValue('--type')):
        print("Checking tracks....")
        err = 0
        for track in data["media"]["track"]:
            d = json.dumps(track, indent=4) # json.dumps(data) converts the dictionary into a JSON string.
            if(a.hasOptionValue('--key')):
                print(track[a.getOptionValue('--key')])
            else:
                print(d)
            err = 0
            break
        else:
            err = 1
        if(err):
            print("Unable to fetch track")
        else:
            json.dumps(data, indent=4)
else:
    print_help()

