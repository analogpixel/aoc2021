Day 2: https://adventofcode.com/2021/day/2

Part 1
https://mathematica.stackexchange.com/questions/120370/replace-part-on-string-in-list
In[202]:= input = ReadList["/Users/mattpoepping/aoc2021/day02/input_1.txt", String];
Times @@ Total[  Map[ ToExpression[ StringReplace[#, {"forward" -> "{1,0}*", "down" -> "{0, 1}*", "up" -> "{0,-1}*" }] ]&, input ]] 
Out[203]= 2187380

Part 2
In[176]:= input = Import["/Users/mattpoepping/aoc2021/day02/input_1.txt", "Table"];
m := Function[ {loc,cmd},  Which[ 
StringContainsQ[ cmd[[1]], "down"], loc + {0,0,cmd[[2]]},
StringContainsQ[cmd[[1]], "up"], loc + { 0,0, -1 * cmd[[2]]},
StringContainsQ[cmd[[1]], "forward"], loc + { cmd[[2]], loc[[3]] * cmd[[2]], 0},
True, loc
]
]
output = Last[FoldList[ m, {0,0,0}, input]];
output[[1]] * output[[2]]
Out[179]= 2086357770
