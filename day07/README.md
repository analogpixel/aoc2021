[day 7](https://adventofcode.com/2021/day/7)

## Read in data
```mathematica
data = ReadList["FILENAME", Number, RecordSeparators -> ","];
```
## Part 1

Brute force, look at each combination of distances and see which total comes out the smallest:

```mathematica
First[SortBy[ Map[ Function[{x}, {x, Total[Map[ Abs[# - x] &, data]]}], Range[Min[data], Max[data]] ], #[[2]] &]] 
```

## Part 2

update the distance calculation to just add the range of the distance.

```mathematica
First[ SortBy[ Map[ Function[{x}, {x, Total[Map[ Total[Range[ Abs[# - x]]] &, data]]}], Range[Min[data], Max[data]] ], #[[2]] &]]
```
