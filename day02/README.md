[Day 2](https://adventofcode.com/2021/day/2)

## Part 1

map strings to expressions that will be evaluated(ToExpression).

```mathematica
input = ReadList["filename", String];
Times @@ Total[  Map[ ToExpression[ StringReplace[#, {"forward" -> "{1,0}*", "down" -> "{0, 1}*", "up" -> "{0,-1}*" }] ] &, input ]]
```


## Part 2

Same concept as above, but a little more logic to handle the aim.

```mathematica
input = Import["filename", "Table"];
m := Function[ {loc, cmd},  Switch[ cmd[[1]], 
   "down", loc + {0, 0, cmd[[2]]},
   "up", loc + { 0, 0, -1 * cmd[[2]]},
   "forward", loc + { cmd[[2]], loc[[3]] * cmd[[2]], 0}
   ]
  ]
Times @@ Last[FoldList[ m, {0, 0, 0}, input]][[1 ;; 2]]
```

