#!/usr/bin/env python
import operator
import sys
import os

logfile = ""
top = 10;

def usage():
    if len(sys.argv) < 2:
        print 'This script is used for checking how many same lines from input file\n'
        print 'Usage: ' + sys.argv[0] + ' <FILE> <NUMBER>'
        print '    FILE. Required, input file name'
        print '    NUMBER. Optional, print first NUMBER lines instead of first 10'
        sys.exit(0)

usage()

if len(sys.argv) >= 2:
    logfile = sys.argv[1]
if len(sys.argv) >= 3:
    top = int(sys.argv[2])

table = {}
if os.path.isfile(logfile):
    for line in open(logfile):
        line = line.strip()
        if not table.get(line):
            table[line] = 1
        else:
            table[line] += 1
else:
    print "File: " + logfile + " doesn't exist."
    sys.exit(0)

sorted_table = sorted(table.items(), key=operator.itemgetter(1), reverse=True)

print "Statistics:\n"
for x in sorted_table[:top]:
    print x[1], ": ", x[0]