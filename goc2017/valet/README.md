Daenerlisp Targzipper has decided to hold a tournament celebrating her Nameday. She has invited the Bothpaki horde, and as a result, it has been determined that there simply aren't enough horse stables in Lizardrock! Her advisors have worked feverishly and have built multi-level horse stables, which they propose will solve the imminent horse-stabling challenges.

Each level of the stables has a maximum capacity. Dropping off or picking up a horse takes a number of minutes equal to the level on which the horse is stabled. Stabling a horse on the first level takes one minute, the second level takes two minutes, the third level takes three minutes, etc...

Given a schedule of appointments with drop off dates and stay durations, find the minimum amount of time you will need to spend dropping off or picking up horses.

You can assume that at any time there will never be more horses scheduled than the stable's maximum capacity. You can also assume that there is a valid solution without needing to move horses between levels during their stay.

Input will be read from stdin and will have the following format:

```
level1_capacity level2_capacity level3_capacity ...
horse1_arrival_day horse1_stay_length
horse2_arrival_day horse2_stay_length
horse3_arrival_day horse3_stay_length
...
```

The first horse and the first floor are number 1 (so, not zero-indexed), and stay length is an integer greater than 0.

What you should output is what floor each horse goes onto such that you spend the minimum time picking up and dropping off horses (Bothpaki Plasma Cowboys are not known for their patience). There may be multiple optimal answers.

```
horse_num floor_num
horse_num floor_num
...
```

### Example

#### Input

```
1 1 1
0 3
1 2
2 1
```

#### Output

For this example there are multiple possible valid outputs. Here are two:

```
1 1
2 2
3 3
```

```
1 3
2 2
3 1
```

#### Explanation

We'll explain the first output. We are given a 3-level stable with one stall on each level. There will be 3 horses.

Day 0
: The first horse comes in for three days. We put the first horse on the first floor, so it takes one minute to drop off.

Day 1
: The second horse comes in for two days. We put it on the second level as the first level is taken. It takes two minutes to drop off.

Day 2
: The third horse comes in for one day and we can now only put it on the third level since there is no more space anywhere else. This takes three minutes to drop off.

End of day 2
: Pick up horses 1, 2, and 3. This takes six minutes.

Adding those times up we get 12 minutes of work, and horse 1 goes to floor 1, horse 2 goes to floor 2, and horse 3 goes to floor 3.
