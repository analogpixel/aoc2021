[day 3](https://adventofcode.com/2021/day/3)

## Part 1

Get a list of columns, for each column sum it up and see if there are more 0's or 1's, then
invert that list to get epsilon. convert those 2 binary strings into numbers and multiply them together.

```mathematica
input = ReadList["filename", String];
gama =  If[ # > Length[input]/2, 1, 0] & /@ Total[ ToExpression /@ StringSplit[#, ""] & /@ input , {1} ] ;
epsilon = Map[ If[# == 0, 1, 0] &, gama];
FromDigits[gama, 2] * FromDigits[epsilon, 2]
```

## Part 2

Prety messy and can be cleaned up a lot.

```mathematica
input = ReadList["filename", String];

fox = Function[{inp}, 
   lst = inp[[1]];
   i = inp[[2]];
    mc = 
    ToString[
     First[
      ReverseSort[
       Commonest[ (ToExpression /@ StringSplit[#, ""] & /@ lst )[[ 
         All, i]] ]  ] ] ] ;
   {
    Select[ lst, Function[ {str}, StringTake[str, {i}] == mc ] ],
    i + 1
    }
   ];

fscrub = Function[{inp}, 
   lst = inp[[1]];
   i = inp[[2]];
   lc = ToString[
     First[
      ReverseSort[
       Commonest[ (ToExpression /@ StringSplit[#, ""] & /@ lst )[[ 
         All, i]] ]  ] ] ];
   {
    Select[ lst, Function[ {str}, StringTake[str, {i}] != lc ]],
    i + 1
    }
   ];

  FromDigits[ NestWhile[ fox, {input, 1}, Length[ #[[1]] ] > 1 & ][[1]] [[1]], 2]

  FromDigits[ NestWhile[ fscrub, {input, 1}, Length[ #[[1]] ] > 1 & ][[1]] [[ 1]], 2]
  ```
