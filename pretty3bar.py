#! /usr/bin/python3

import sys
import json
from subprocess import call

def parseVersion():
    version = json.loads(sys.stdin.readline().rstrip())['version']
    print("i3bar protocol version : v" + str(version))

def stripStreamBeginning():
    line = sys.stdin.readline().rstrip()
    if line != "[":
        raise Exception("Line after version should be the '[' beginning the"
                "array")

def parseStream():
    for line in sys.stdin:
        line = line.rstrip()
        if line[0] == ',':
            line = line [1:]
        elements = json.loads(line)
        out = []
        for e in elements:
            if len(e['full_text']) != 0:
                out.append(e['full_text'])
        call('color ' + 'a', shell=True)
        print(" | ".join(out))

parseVersion()
stripStreamBeginning()
parseStream()

# Parsing main string
