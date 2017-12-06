#!/usr/bin/env python3

import csv
import numpy as np

def read_tsv(tsv):
    return [ [ int(s) for s in line ] for line in csv.reader(tsv, dialect="excel-tab") ]

def redistribute(banks,blocks):
    even = np.floor(blocks / banks)
    spill = blocks%banks
    diff = np.array([ even+1 if bank < spill else even for bank in range(banks) ])
    diff[-1] -= blocks
    return diff
    
def changes(bank,banks,blocks):
    return [ int(d) for d in np.roll(redistribute(banks,blocks),bank+1) ]

def most_blocks(state):
    m=max(state)
    return state.index(m)

def step(state):
    m = most_blocks(state)
    diff = changes(m, len(state), state[m])
    return [ s+d for s,d in zip(state,diff) ]

with open("06.input") as tsv:
    data=read_tsv(tsv)[0]

data=[0,2,7,0]

print(data)
state=data
steps=0
seen={}
while not tuple(state) in seen.keys():
    seen[tuple(state)]=steps
    state = step(state)
    steps+=1
    print(steps,tuple(state))

print(steps,steps-seen[tuple(state)])