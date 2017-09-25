You've just landed a job re-shelving books in the Bastion's library!

As an initiate to the Lineup of Masters, you've been assigned to return books
in the library. Due to a severely outdated system, the floor on which
each book is to be re-shelved comes as a sequence of commands. A `+` represents
ascending a floor, while a `-` represents descending a floor.

Your master requires all initiates to keep track of the position of any
command in a sequence that would cause them to enter the library's restricted
section&#8212;floor -1 or lower.

The library is very large and you will never find the top or bottom floors.

The returns room, where books are received and prepared for re-shelving, and from which all sequences of commands are assumed to start, is located in the basement (floor 0).

To ensure books are re-shelved accurately and in a timely fashion, determine a way to know the (1-indexed) position of each command that will cause you to enter the restricted section.

### Example

#### STDIN

```
-+-++---
```

#### STDOUT

```
1
3
7
```

#### Explanation

1. `-` tells you to go from floor 0 to floor -1.
1. `+` tells you to go from floor -1 to floor 0.
1. `-` tells you to go from floor 0 to floor -1.
1. `+` tells you to go from floor -1 to floor 0.
1. `+` tells you to go from floor 0 to floor 1.
1. `-` tells you to go from floor 1 to floor 0.
1. `-` tells you to go from floor 0 to floor -1.
1. `-` tells you to go from floor -1 to floor -2.

Commands 1, 3, and 7 caused you to enter the restricted section (go from floor 0 to floor -1).
