# Overbond's Coding Challenge
Presented by Rio Kivell

### There are two Problems in this Challenge

For a full description of the original problems, check out https://gist.github.com/kseyon/fdb3ede4fadc2559c74fcdbe32ccf613

# How to Execute the Solutions

There is a Makefile included in the solutions.  To run Solution 1, simply call:

```
make yield sample1.csv
```

For Solution 2, call:

```
make curve sample2.csv
```

You can replace ```sample1.csv``` and ```sample2.csv``` with whatever file(s) you'd like to run the solution scripts on.  I've submitted my solutions with 5 sample csv's, following the naming convention established above.

You can also call ```make test all``` to run a suite of 5 tests, and see their output in stdout.

## Problem One
The first problem is to create a script that will calculate the yield spread, or return, between a corporate bond and its government bond benchmark.

## My Solution
My answer to this problem is in ```yield.py```.

### Choices/Tradeoffs I Made In This Solution

* I chose to implement a solution that reads from files and writes to stdout, as opposed to reading from stdin/writing to files, because I find it a cleaner and more understandable method for executing scripts like these in the command line.
* I used a simple O(n^2) solution in the main logic, when comparing each corporate bond to each government bond.  Had I more time, I might've tried a faster method to find the closest government bond to each corporate one.

## Problem Two
The next challenge is calculate the spread to the government bond curve, using linear interpolation.

## My Solution
My answer to this problem is in ```curve.py```.

### Choices/Tradeoffs I Made In This Solution

* Similar to above, I read from files and output to stdout.
* On lines 22-29 of curve.py: I could have simply used the original values I set x1, y1, x2, and so on to, in the final calculation, rather than simply rename them.  I wanted to do so to make the calculation more readable, and understandable to someone with experience manipulating graphs/cartesian points.  I sacrifice a little bit of time for a lot of clarity.
* I sort the bonds in the input file as I insert them into government_bonds and corporate_bonds, in order to save myself the time of sorting them later.