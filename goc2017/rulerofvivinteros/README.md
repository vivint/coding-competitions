In the latest popular tabletop game Ruler of Vivinteros, the Lansisters,
Sparks, Greyhats, Targzippers and other families all compete to rule
Vivinteros by rolling dice and acquiring power ups. When a certain power up
is acquired, rolling a straight with the dice will demolish the competition.

### Instructions

Daenerlisp Targzipper decides to figure out the odds of getting a straight
to decide if she should pursue the power up. She gets ambitious and decides
to calculate the probability of getting a straight (all numbers once from 1
to \\(N\\)) for rolling \\(N\\) number of \\(N\\)-sided dice with \\(C\\)
number of throws. Help Daenerlisp calculate the probability.

To clarify, when a throw of the dice is performed, all of the dice involved in
the throw are thrown at the same time. However, after the first throw, the
roller gets to decide which dice to reroll and which to keep. Assume that
Daenerlisp will choose which dice to reroll optimally. The number of dice
rolled is equal to the number of sides on each die.

Over stdin, you are provided with two numbers: \\(N\\) which is both the number
of sides on each die and the total number of dice and \\(C\\) the maximum
number of throws of the dice. \\(2 \le N \le 8\\) and \\(1 \le C \le 8\\).

Output the probability as a percentage to four decimal places after the
decimal. Round the last decimal place.

### Example

A two sided die is essentially a coin and the case of \\(N = 2\\) is much
easier than larger \\(N\\). The exact probability for only 2 dice is
also very easy: \\(1-0.5^C\\) which equals \\(99.6094\%\\) for \\(C = 8\\).

#### Input

```
2 8
```

#### Output

```
99.6094
```
