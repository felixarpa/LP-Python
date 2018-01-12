#!/usr/bin/python3
import argparse
from api import get_actes_as_xml
import sys
from keytree import KeyTree

parser = argparse.ArgumentParser()
parser.add_argument("--key")
#parser.add_argument("query", type = str)
args = parser.parse_args()
#print(args.search)
#print(args.query)

if args.key:
    print(eval(args.key))

def show_all(root, blanks):
    print(blanks, root.tag, root.attrib, root.text)
    for child in root:
        showAll(child, blanks + "  ")

#show_all(get_actes_as_xml(), "")

#print(sys.argv[1], sys.argv[2])
