[day 6](https://adventofcode.com/2021/day/7)

## Part 1
this is the wrong way to do things to get the answer.  it works, but is too slow to actually complete part 2

Subtract 1 from every number in the list, and then replace -1 with {6,8} 

```mathematica
data = ReadList[ "FILENAME", Number, RecordSeparators -> ","];
Length[ Nest [ Flatten[  Map[ # - 1 &, #] /. -1 -> {6, 8}] & , data, 80]]
```

## Part 2

The correct(er) way to do things. Bucket shifting. you have buckets for -1 all the way to 8, and you 
just shift buckets around.

```mathematica
data = Tally[ ReadList["/Users/mattpoepping/aoc2021/day06/input_1.txt", Number, RecordSeparators -> ","]]

{{3, 58}, {5, 67}, {2, 70}, {4, 48}, {1, 57}}

Total[ Nest [ Join [ #[[2 ;; 7]], {#[[8]] + #[[1]]}, {#[[9]]}, {#[[1]]} ] & , {0, 0, 57, 70, 58, 48, 67, 0, 0, 0},  257]]
```
