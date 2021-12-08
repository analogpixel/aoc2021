# [day 8](https://adventofcode.com/2021/day/8)

## Part 1

this is the easy part, just look for strings that match a length

```mathematica
data = Import["filename", "Table"]; Length[ Select[ 
StringLength /@ Flatten[ Map[ StringSplit[#, " "][[12 ;;]] &, data]],  MemberQ[{2, 4, 3, 7}, #] &]]
```

## Part 2

this is the harder part, you need to figure out based on known values what the other values are:

```mathematica
convsegs2 =  Function[{a},
   y = Map[ Sort[#] &, a];
   seg1 = SelectFirst[ y, Length[#] == 2 &];
   seg4 = SelectFirst[ y, Length[#] == 4 &];
   seg7 = SelectFirst[ y, Length[#] == 3 &];
   seg8 = SelectFirst[ y, Length[#] == 7 &];
   seg9 = SelectFirst[ y, Length[#] == 6 && ContainsAll[#, seg4] &];
   seg0 = SelectFirst[ y, Length[#] == 6 && ContainsAll[#, seg7] && # != seg9 &];
   seg6 = SelectFirst[ y, Length[#] == 6 && # != seg9 && # != seg0 & ];
   seg5 = SelectFirst[ y, Length[#] == 5 && ContainsAll[# , Complement[seg9, seg1]  ] &];
   seg3 = SelectFirst[ y, Length[#] == 5 && # != seg5 &&  ContainsAll[#, seg7] &];
   seg2 = SelectFirst[y, Length[#] == 5 && # != seg5 && # != seg3 &];
   z = Map[ Replace[#, {seg1 -> 1, seg2 -> 2, seg3 -> 3, seg4 -> 4, seg5 -> 5, seg6 -> 6, seg7 -> 7, seg8 -> 8, seg9 -> 9, seg0 -> 0} ] &, y];
   FromDigits[ z[[-4 ;;]]]
   ];
 

b = Map[ StringSplit[#, ""] &, Select[#, Function[{x}, x != "|"]] & /@   Map[ Flatten[ StringSplit[#, " "]] &, data]];
Total[Map[ convsegs2, b]]
```
