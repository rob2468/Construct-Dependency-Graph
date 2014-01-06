#!/usr/bin/env python
from gensimudata import P

import time

def ConstructDepGraph(V, E):
    for p in P:
        for d in p.dpro:
            if not (d in V):
                V.append(d)
            for d1 in p.duse:
                if not (d1 in V):
                    V.append(d1)
                E.append((d, d1))

if __name__=="__main__":
#     print P
    starttime = time.time()
    V = []
    E = []
    ConstructDepGraph(V, E)
    endtime = time.time()
    print (endtime-starttime)*1000, "ms"
