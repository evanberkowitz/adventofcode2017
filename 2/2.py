#!/usr/bin/env python3

import csv

def read_tsv(tsv):
    return [ [ int(s) for s in line ] for line in csv.reader(tsv, dialect="excel-tab") ]

def check(line):
    mx=max(line)
    mn=min(line)
    return mx-mn

def div_check(line):
    return int([ a/b for a in line for b in line if a%b==0 and a!=b ][0])

with open("2.input") as tsv:
    data=read_tsv(tsv)
    linechecks=[ check(line) for line in data ]
    print("Sum of largest differences on each line = ",sum(linechecks))

    divchecks=[ div_check(line) for line in data ]
    print("Sum of integer quotients on each line = ",sum(divchecks))

