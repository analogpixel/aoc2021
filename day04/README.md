[day 4](https://adventofcode.com/2021/day/4)

## Data
read in the data

```mathematica
data = Import["filename", "Table"];
bingocalls = Map[ ToExpression, StringSplit[First[data], ","][[1]]];
bingocards = DeleteCases[ SplitBy[ Rest[data], # == {} & ], { {} }];
```

## Functions
```mathematica
checkCard[crd_, lst_] := AnyTrue[ Map[ ContainsAll[ lst, #] &, crd] , TrueQ ] || AnyTrue[ Map[ ContainsAll[ lst, #] &, Transpose[crd] ], TrueQ];
score[wincrd_, i_] := (Total[ Total[ wincrd]] - Total[ Intersection[ Flatten[ wincrd] , bingocalls[[1 ;; i]] ]]) * bingocalls[[i]];
```

## Part 1
figure out the first person to bingo

```mathematica
i = 1; While[  !  AnyTrue[  Map[checkCard[#, bingocalls[[1 ;; i]] ] &, bingocards], TrueQ],  i++ ] ;
wincrd = First[Select[ bingocards, AnyTrue[  Map[  checkCard[#, bingocalls[[1 ;; i]]  ]], TrueQ] & ]];
score[wincrd, i]
```

## Part 2
Then I just got lazy and handjammed it; increase the card count until you only have
one card left, then calculate the score on that card:

```mathematica
lastcrd = Select[ bingocards, !  AnyTrue[  Map[  checkCard[#, bingocalls[[1 ;; 85]]   ]], TrueQ] & ]
score[ First[lastcrd], 86]
```

