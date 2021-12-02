```
Day 1 part 1
In[38]:= datafile = "/Users/mattpoepping/aoc2021/day01/input_1.txt";
Length[ Select[ Differences[ReadList[datafile]], # > 0 &]]
Out[39]= 1502
Day 1 part 2
In[40]:= datafile = "/Users/mattpoepping/aoc2021/day01/input_1.txt";
Length[ Select[ Differences[ReadList[datafile],1,3], # > 0 &]]
Out[41]= 1538
this version uses ListConvolve to add each group of three, then comes back and finds the differences between that resulting list:
In[60]:= datafile = "/Users/mattpoepping/aoc2021/day01/input_1.txt";
Length[ Select[ Differences[ ListConvolve[ {1,1,1}, ReadList[datafile]] ], #> 0&]]
Out[61]= 1538
```
