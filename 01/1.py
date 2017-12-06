#!/usr/bin/env python3

with open('1.input','r') as f:
    data=f.read()

print("Input number=",data)

# Get the index of the element shift items ahead of idx, accounting for periodic length.
def n(length,shift,idx):
    return (idx+shift)%length

def acc(data,shift):
    total=0
    l=len(data)
    for i in range(l):
        if data[i] == data[n(l,shift,i)]:
            total+=int(data[i])
    return total

print("Look-ahead=",1,":",acc(data,1))

print("Look-ahead=",int(len(data)/2),":",acc(data,int(len(data)/2)))