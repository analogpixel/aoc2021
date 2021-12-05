[day 5](https://adventofcode.com/2021/day/5)

## Part 1

### Setup
```mathematica
data =  Import["filename", "String"];
data =  Partition[ Map[ToExpression,  StringSplit[ StringReplace[data, {" -> " -> ",", "\n" -> "," } ], ","] ], 4];

linepts[x1_, y1_, x2_, y2_] := Which[ x1 == x2, Map[ {x1, #} &, Range[Min[y1, y2], Max[y1, y2] ]], y1 == y2, Map[ {#, y1} &, 
   Range[Min[x1, x2], Max[x1, x2]]], True, {} ]
```

### Solve

`linepts` returns all the points a line is made up of, so I take those points and Tally up how many of them overlap.

```mathematica
d = Tally[ Partition[ Flatten[ Map [ Apply[ linepts, # ] &, data]], 2]] ;
Length [ Select[d, #[[2]] >= 2 &]]
```

## Part 2

### Setup
The hardest part sometimes feels like figuring out how to load the data.

The linepts formula is changed to handle 45d lines.  all that math is me being to lazy to define two
variables for the line formula, but it comes down to figuring out y=mx+b  and returning the points on the line.

```mathematica
data =  Import["FILENAME", "String"];
data =  Partition[ Map[ToExpression,  StringSplit[ StringReplace[data, {" -> " -> ",", "\n" -> "," } ], ","] ], 4];

linepts[x1_, y1_, x2_, y2_] := Which[ 
  x1 == x2, Map[ {x1, #} &, Range[Min[y1, y2], Max[y1, y2] ]], 
  y1 == y2, Map[ {#, y1} &, Range[Min[x1, x2], Max[x1, x2]]], 
  True, Map[ {#, # * ((y2 - y1)/(x2 - x1)) + (y1 - ((y2 - y1)/(x2 - x1))* x1)} &, Range[Min[x1, x2], Max[x1, x2]]]
  ]
```

### Solve
```mathematica
d = Tally[ Partition[ Flatten[ Map [ Apply[ linepts, # ] &, data]], 2]] ;
Length [ Select[d, #[[2]] >= 2 &]]
```
