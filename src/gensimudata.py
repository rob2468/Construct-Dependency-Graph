#!/usr/bin/env python
from data import DNUM
from data import PNUM
from datamodel import proc

import random

datafiles = []
for i in range(DNUM):
    datafiles.append(i)

# process nodes in provenance graph
P = []
dsum = DNUM
for i in range(PNUM):
    # calculate p[i]'s data files number, (input number + output number)
    avg = dsum/(PNUM-i)
    var = random.randint(0, dsum)
    if avg!=0:
        dev = abs(var-avg)*1.0/avg
        if dev>0.75:
            var = avg
    if i==PNUM-1:
        var = dsum
    
    # update dsum: remaining data file number in each iteration
    dsum -= var
    
    # split var in two parts: one for input, and one for output
    avg = var/2
    temp = random.randint(0, var)
    if avg!=0:
        dev = abs(var-temp)*1.0/avg
        if dev>0.75:
            temp = avg
    ndpro = temp
    nduse = var-temp
    
    # assign values to each process node
    dpro = []
    duse = []
    for j in range(ndpro):
        item = datafiles.pop(random.randint(0, len(datafiles)-1))
        dpro.append(item)
    for j in range(nduse):
        item = datafiles.pop(random.randint(0, len(datafiles)-1))
        duse.append(item)
    p = proc(dpro, duse)
    P.append(p)

if __name__=="__main__":
    pass
