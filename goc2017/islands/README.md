In the event that an undead army overruns all of Vivinteros, you've been commanded to come up with an evacuation plan. After weeks of planning and reconnaissance, the masters have drafted a list of suitable islands, and you've been tasked with making the final decision. However there is one problem: each island has different resource quantities available and you must make the right multi-criteria decision to save humanity. The masters have identified nine critical resources available on each island and prioritized them as follows:

| Resource    | Priority |
|-------------|----------|
| Water       |     0.30 |
| Wood        |     0.15 |
| Coal        |     0.10 |
| Iron        |     0.05 |
| Stone       |     0.10 |
| Obsidian    |     0.15 |
| Copper      |     0.05 |
| Gold        |     0.03 |
| Silver      |     0.07 |

### The problem

Your program should read from stdin the resource quantities of each island, in the order specified by the table above, as nine space-separated floating-point values. Each line represents a single island. Your program must use [Weighted Product Model](https://en.wikipedia.org/wiki/Weighted_product_model) analysis to rank the islands based on the priorities prescribed by the masters above. Use the resources quantities received via stdin, and output the islands by number in ranked order from best to worst to stdout. So, in the below example, the island that has a `5000` resource for water is the most preferable island, and the island with a `1000` resource for water is the least preferable.

Note: Each resource is expected to be a positive floating-point value and while each value has a different unit of measure (gallons, ounces, pounds, etc.), your program should be independent of any units of measure.

*Update:* we don't want to change this problem too much in light of how many people have already tried it, but I just want to take one more stab at making something unambiguous. Many people have been confused about whether the output should be the island index ordered by rank, or the island rank ordered by index. We're asking for the island index ordered by rank.

### Example

#### Input

```
3000 5000 50 100 1000 2000 50 20 30
2000 6000 100 400 500 1000 40 70 131
5000 2000 900 100 400 5000 1 10 56
500 1000 100 200 500 10000 42 99 1000
500 2000 1500 10 500 9000 100 200 400
1000 1000 2000 10 500 100 100 200 4000
```

#### Output

```
2
1
0
4
3
5
```
