#!/usr/bin/env python3

import argparse 

parser = argparse.ArgumentParser(
    usage = '%(prog)s -d [domain name]' 
    )
#add a description some time

### define arguments to be used. Might add more some time, using argparse for future changes. 
parser.add_argument("-d","--domainname", type=str, required=True, help='Target domain name')

args = parser.parse_args()

