#!/usr/bin/env python
import pdb

def strprint(s1, i1):
    if i1 == 1:
        return s1
    else:
        return (s1 +  strprint(s1,i1-1))

def main():
    s = 'roger'
    i = 3
    s2 = strprint(s,i)
    print s2

if __name__ == "__main__":
    main()

