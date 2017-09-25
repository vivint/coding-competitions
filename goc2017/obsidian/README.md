As an obsidian smith, trade has been picking up lately. This is great news! But it's also forced you to streamline your processes. Today you've decided to streamline the process for determining if a specific piece of obsidian is suitable to be shaped into multiple specific weapons. A piece of obsidian is suitable if it's large enough and wouldn't leave any flaws or impurities in the crafted weaponry.

### Input

The first line of input will contain the number of weapons desired \\(M\\), and the number of pieces of obsidian \\(N\\). The value of \\(M\\) will be between 1 and 10 inclusive, while \\(N\\) can range from 1 to 100 inclusive.

The following \\(M\\) lines describe the weapons desired. Each weapon has a length \\(L\\) between 1 and 9 inclusive, indicated by repeating the weapon's 0-based index a number of times equal to \\(L\\). For example, if the third weapon's desired length is four units, it would be represented as `2222`.

The next lines describe each piece of obsidian available for crafting the desired weapons. An obsidian description starts with a line containing the number of columns \\(x\\) and rows \\(y\\), where \\(x \times y \le 100\\). Following the columns and rows is a grid \\(x\\) columns wide by \\(y\\) rows long describing the obsidian to be used. A `d` represents obsidian suitable for crafting, while an `x` represents a flaw or impurity in the obsidian that makes it unsuitable for crafting.

### Output

For each piece of obsidian, print a line containing one number; `1` if all of the desired weapons can simultaneously be crafted out of this specific piece of obsidian, or `0` otherwise. The expected output should contain \\(N\\) lines of `1` or `0`.

Weapons will never be placed diagonally.

### Examples

#### Input

```
3 2
0000
11
222
4 3
dddd
ddxx
dddx
5 2
xxddd
ddddd
```

This input requests that we determine if three weapons be crafted from each of two pieces of obsidian.

The first weapon has a length of four units. The second a length of two units, and the third a length of three units.

The first piece of obsidian is four units wide by three units long. It has three unsuitable sections, indicated by `x`s.

The second piece of obsidian is five units wide by two units long. It has two unsuitable sections, indicated by `x`s.

#### Output

```
1
0
```

#### Explanation

In the first obsidian above, we can cut the glass like this:

```
0000
11xx
222x
```

However, the second one can't satisfy all the weapon requirements, particularly weapon 3.

```
xx222
0000d
```
