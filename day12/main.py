#!/usr/bin/env python

data = {}
verts = []

for r in open("input_1.txt","r"):
    (a,b) = r.strip().split("-")
    
    if not a in data:
        data[a] = []
    if not b in data:
        data[b] = []

    if b not in ["start"]:
        data[a].append(b)
    if a not in ["start"]:
        data[b].append(a)

    if a not in verts:
        verts.append(a)
    if b not in verts:
        verts.append(b)


def findpaths(currentpath, v):
    # loop through all connected nodes
    for j in data[v]:
        if j == "end":
            print( currentpath + [v] + ["end"] )
        elif j.islower() and j in currentpath:
            continue
        else:
            findpaths(currentpath + [v], j) 

def findpaths2(currentpath, d, v):
    # loop through all connected nodes
    for j in data[v]:
        if j == "end":
            print( currentpath + [v] + ["end"] )
        elif (j ==d and currentpath.count(d) < 2):
            findpaths2(currentpath + [v], d,j) 
        elif (j.islower() and j in currentpath):
            continue
        else:
            findpaths2(currentpath + [v], d,j) 

# part 1
# ./main.py  | sort -u | wc -l
# findpaths([], "start")

# part 2
# ./main.py  | sort -u | wc -l
for a in verts:
    if a.islower():
        findpaths2([], a, "start")
