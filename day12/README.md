[day12](https://adventofcode.com/2021/day/12)

I cheated and used python for this one, the mathematica graph 
functions don't revist nodes, and ` ¯\_(ツ)_/¯ `

## Load the data
```python
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
```

## Part 1
```python
def findpaths(currentpath, v):
    # loop through all connected nodes
    for j in data[v]:
        if j == "end":
            print( currentpath + [v] + ["end"] )
        elif j.islower() and j in currentpath:
            continue
        else:
            findpaths(currentpath + [v], j) 

```

## Part 2
```python
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

```

So lazy, just run the programs with `| sort -u | wc -l `    
