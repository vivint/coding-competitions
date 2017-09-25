Congratulations! You've received an
<acronym title="Request for proposal">RFP</acronym> to build The Scarlet Keep's
"Dark Cells".

You have the option of choosing between different types of cells to build, but
you must find the right assortment of cells to maximize the number of prisoners
contained while minimizing the cost to build.

Eyegone the Conquistador has been reigning with an iron fist so there's no shortage
of prisoners. On the other hand, the King's advisor has told you that building
codes require that your prison expect no more than \\(P\\) criminals imprisoned
at a time. Some dark cells are multi-tenant and can host more than one
prisoner. Expect that if you build a dark cell, it will always be in use.

For every dark cell option there are two values--the number of prisoners it
can handle and the amount it costs. You are free to assume both values will
never be less than one. You need to minimize expenses while still providing
cells for exactly \\(P\\) prisoners.

Input will be read from stdin and will have the following format:

```
P
cost1      cost2      cost3      ... costN
prisoners1 prisoners2 prisoners3 ... prisonersN
```

Output will represent minimum cost and how many of each dark cell to purchase.

```
minimum_cost
count1 count2 count3 ... countN
```

### Example

#### Input

```
29
2 5 9
1 3 6
```

#### Output

```
45
2 1 4
```
