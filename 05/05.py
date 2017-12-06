#!/usr/bin/env python3

with open('05.input','r') as f:
    part_1=[int(line) for line in f]

LEFT=0
RIGHT=len(part_1)

spot=0
steps=0

while LEFT <= spot < RIGHT:
    steps+=1
    part_1[spot]+=1
    spot+=part_1[spot]-1
    
print(steps)

with open('05.input','r') as f:
    part_2=[int(line) for line in f]

LEFT=0
RIGHT=len(part_2)

spot=0
steps=0

while LEFT <= spot < RIGHT:
    steps+=1
    offset = part_2[spot]
    if(offset >=3):
        part_2[spot]-=1
    else:
        part_2[spot]+=1
    spot+=offset
    
print(steps)