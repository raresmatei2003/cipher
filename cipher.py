#!/usr/bin/python3

import sys      # gives access to cli arguments

def main():
    f=open("cipher.txt","r")
    s=f.read()
    m={"I":"A",
    "L":"O",
    "J":"S",
    "P":"I",
    "O":"T",
    "U":"E",
    "V":"L",
    "Z":"M",
    "B":"D",
    "Q":"P",
    "S":"N",
    "K":"F",
    "T":"R",
    "W":"C",
    "G":"B",
    "F":"H",
    "H":"G",
    "X":"U",
    "R":"W",
    "N":"K",
    "M":"J",
    "E":"V",
    "D":"X"}
    for i in range(0,len(s)):
        if s[i] in m.keys():
            print("\033[1;31m" + m[s[i]] + "\033[0m", end='')
        else :
            print(s[i], end='')
main()
print('\n')