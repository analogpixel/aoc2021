[day 9](https://adventofcode.com/2021/day/9)

## Part 1
Due to trickery with the pepople that supply the data, one of the columns starts with a 0, which causes some issues, thus the padleft to fix them.

```mathematica
data = PadLeft[#, 100] & /@  Flatten [ IntegerDigits /@   Import["/Users/mattpoepping/aoc2021/day09/input_1.txt", "Table"], 1 ]; 

getxy = Function[ {lst, x, y, default},  {h, w} = Dimensions[lst];  If[ x > 0 && x <= w && y > 0 && y <= h, lst[[y, x]], default]];
lowpointq = Function[ {x, y, lst}, pt = lst[[y, x]]; If[ getxy[lst, x + 1, y, 99999] > pt && getxy[lst, x - 1, y, 99999] > pt && getxy[lst, x, y + 1, 99999] > pt && getxy[lst, x, y - 1, 99999] > pt, True, False] ]; 

lowpoints = Select[ Flatten[ MapIndexed[ {#1, #2, lowpointq[ #2[[2]], #2[[1]], data] } &, data, {2}], 1], #[[3]] & ];

Total[#[[1]] + 1 & /@ lowpoints]
```

## Part 2
The only thing you really need for part 2 is floodfill, which will look at each low point and figure out the basin size.  Take
each one of the low points you figured out in part1 and then use floodfill to figure out how big that basin is.

```mathematica

floodfill = Function [{lst, x, y, wall}, 
    stack = {{x, y}} ;
    filled = {};
   While[  Length[stack] > 0,
    {{xa, ya}, stack} = {First[stack], Rest[stack]};
    If[ xa > 0 && xa <= Dimensions[lst][[2]] && ya > 0 && 
      y <= Dimensions[lst][[1]] && 
      lst[[ya, xa]] != wall && ! MemberQ[filled, {xa, ya}], 
     filled = Append[filled, {xa, ya}];
     stack = 
      Join[ 
       stack, { {xa + 1, ya}, {xa - 1, ya}, {xa, ya + 1}, {xa, 
         ya - 1}}];
     ]
    ];
   filled
   ];

Times @@ ReverseSort[ Map[ Length[floodfill[ data, #[[2]][[2]], #[[2]][[1]], 9]] &, lowpoints]][[1 ;; 3]]
```
