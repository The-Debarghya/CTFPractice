#!usr/bin/python2.7
import pickle

f = open('donotshare')

o = pickle.load(f)

outstr = ''
for line in o:
    for char,n in line:
        outstr += char*n
    outstr += '\n'
print(outstr)
