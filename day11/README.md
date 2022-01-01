[day11](https://adventofcode.com/2021/day/11)

## Init
Load in the data, and setup the function that adds 1 to each neighbor.  

```mathematica
data = Flatten[ 
   IntegerDigits /@ 
    Import["FILENAME", "table"], 1];
ones = data/data;
{dimx, dimy} = Dimensions[data];

(*addSubMatrix takes x,y and adds 1 to all the neighbors,returning \
that list;take the default 1 matrix,and padd it to where it needs to \
go,then chop it down to size.*)

addSubMatrix[{y_, x_}, lst_] := 
 ReplacePart[ 
  ArrayPad[
     {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}, {{y - 1, dimy*2}, {x - 1, 
       dimx*2}}
     ][[2 ;; dimy + 1, 2 ;; dimx + 1]] + lst
  , {y, x} -> -10000
  ]
```
## Part 1 and 2

1. add 1 to all the data
2. check for which locations are over 9
3. add 1 to all the neighbors for locations found in 2
4. goto 2 until no more explosions.
5. count up things, set things back to 0

```mathematica
d1 = data;
flashCount = 0;
Do[ 
 d1 = d1 + ones;
 While[ Length[ Position[ d1, x_ /; x > 9]] > 0,
  d1 = Fold[ addSubMatrix[#2, #1] &, d1, Position[ d1, x_ /; x > 9]] 
  ];
 flashCount = flashCount + Count[ d1, x_ /; x < 0, {2}];
 d1 = d1 /. x_ /; x < 0 -> 0;
 If[ Count[ d1, x_ /; x != 0, {2}] == 0, 
  Print[loopcount]]; (* when they are in sync*)
 , {loopcount, 390}
 ]
d1 // MatrixForm
flashCount
```

