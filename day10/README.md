[day 10](https://adventofcode.com/2021/day/10)

## Part 1

on each line, just push and pop stuff on to a list/stack/whatever and look for where they don't match up

```mathematica
data = Map[ StringSplit[#, ""] &, StringSplit[ Import["filename", "String"], "\n"]];
brackets = <| "[" -> "]", "(" -> ")", "{" -> "}", "<" -> ">" |>;
score = <| "-" -> 0, ")" -> 3, "]" -> 57, "}" -> 1197, ">" -> 25137 |>;

finderror = 
  Function[{lst}, datain = lst; error = "-"; closelst = {}; 
   While[ error == "-" && Length[datain] > 0, 
    If[ 
     (* if this is an open *)
     
     MemberQ[Keys[brackets], 
      First[datain]], {closelst, 
       datain} = {Append[ closelst, First[datain]], Rest[datain]},
     
     (* if this is a close *)
     
     If[ brackets[ Last[closelst] ] == First[datain], 
      {closelst, datain} = {closelst[[1 ;; -2]], Rest[datain]}, (* 
      brackets match *)
      error = First[datain]  (* 
      brackets don't match *)
       ]
     ]
    ];
   error
   ];

Total[ score /@  Map[ finderror, data]]
```

## Part 2
```mathematica
completescore = <| ")" -> 1, "]" -> 2, "}" -> 3, ">" -> 4 |>;
scoreit = Function[{lst}, Fold[ (#1 * 5) + #2 &, 0, lst] ];
```

same as above, except return the unfished sections (and score them)

```mathematica
{error, datain, Map[completescore, Reverse[Map[brackets, closelst]]]}
```

and then get the answer

```mathematica
Median [ Sort[scoreit[#[[3]]] & /@ Select[  Map[ finderror2, data ], #1[[1]] == "-" & ]] ]
```
