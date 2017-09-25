Worshippers of the Plural-Visaged God are a strange and mysterious bunch. From deep within their secretive organization has come what many believe is some sort of puzzle game. Its rules are simple, yet its solution requires great mental acuity.

You are given a box with a specified number of rows and columns, where we
assume the box is rectangular. Each cell in the box contains a 0 or 1.

Given the initial box, the goal is to find the minimum number of columns
that must be "flipped" (0's and 1's swapped in that column) to maximize the
row score. A row adds one point to the score if all its elements are all
0's or all are 1's.

Note for some box configurations there can be more than one minimal solution,
but the problems presented here have a singular, unique solution.

For example, this box has a score of two, as rows 1 and 3 (zero-based)
are uniform with all 0's or 1's.

```
0 0 1 1 0
0 0 0 0 0
1 0 1 0 1
1 1 1 1 1
0 1 1 1 0
```

The input will consist of multiple rows. The first line will contain two
integers separated by a space, specifying the number of rows and columns in
the box. The maximum possible number of rows or columns is 64. Following
this will be a line for each row, conisting of 0's and 1's for each column in
the row, again, separated by spaces.

The output should consist of two lines. On the first line should be a single
number, representing the maximum score after the optimal column flips are
applied. The second line should list the zero-based (from left to right) and
ascending set of columns that are flipped to achieve that maximum score. Again,
you want the maximum score possible, and then from all of the options that
give you the maximum score, you want the one with the minimum column flips.

### Example

#### Input

```
5 5
1 0 0 1 0
1 0 0 1 0
1 0 1 0 0
0 1 1 0 1
1 0 0 1 0
```

#### Output

```
4
0 3
```

The maximum score of 4 is achieved by flipping the leftmost (0) and
second-to-rightmost (3) columns.
