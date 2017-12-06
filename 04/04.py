#!/usr/bin/env python3

with open('04.input','r') as f:
    # chop trailing \n:
    data=[line[:-1] for line in f]

def validate(passphrase):
    words=passphrase.split()
    return int(len(words) == len(set(words)))

test_results=[1,0,1]
test = [ validate(t) for t in ['aa bb cc dd ee', 'aa bb cc dd aa', 'aa bb cc dd aaa'] ]
print( test== test_results )

print("Checking",len(data),"passphrases.")
mask=[ validate(passphrase) for passphrase in data ]
print(sum(mask),"validate correctly.")

def anagram_validate(passphrase):
    words=passphrase.split()
    A = [ ''.join(sorted(w)) for w in words ]
    return int(len(A) == len(set(A)))

print("Checking",len(data),"passphrases for anagram validation.")
mask=[ anagram_validate(passphrase) for passphrase in data ]
print(sum(mask),"validate correctly.")