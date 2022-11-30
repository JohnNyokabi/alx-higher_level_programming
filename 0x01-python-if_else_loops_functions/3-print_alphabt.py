#!/usr/bin/python3
for ch in range(ord('a'), ord('z')+1):
    if ch is not (ord('q')) and ch is not (ord('e')):
        print('{}'.format(chr(ch)), end='')
