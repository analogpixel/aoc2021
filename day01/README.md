
[Day 1](https://adventofcode.com/2021/day/1)

## Part 1

Read in the file, and find the places where the difference between elements is > 0.

```mathematica
Length[ Select[ Differences[ReadList[datafile], 1, 3], # > 0 &]]
```


## Part 2

Use ListConvolve to group the windows, then take the Differences of those windows:

```
ListConvolve[{x, y}, {a, b, c, d, e, f}]
{b x + a y, c x + b y, d x + c y, e x + d y, f x + e y}
```

```mathematica
Length[ Select[ Differences[ ListConvolve[ {1, 1, 1}, ReadList[datafile]] ], # > 0 &]] 
```

