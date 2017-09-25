You've discovered an ancient system of symbols, dating back to the Kids in the Woods. It appears to be a system for denoting an inventory system for counting and comparing various objects, such as sheep, fruit, and tools. In order to better understand the system, you've decided to build an interpreter for the symbols, so you can run them as programs!

In this problem, you're going to build an interpreter for a simple functional
programming language.

### For what programming language?

The programming language you will be interpreting is very simple: there
are three main categories of syntax:

- Literals like `5` or `true`
- Lambda abstraction written `lam <binding> <body>`
- Function application written `app <lambda> <value>`

In case you've never heard the phrase "lambda abstraction" before, a
<em>lambda</em> is simply an anonymous function. In Javascript, `lam x y`
would be written as

```
function(x) { return y }
```

Similarly, function application (`app f x`) would be written `f(x)`. We'll use
`lam x y` and `app f x` because it's a bit simpler.

So, more formally, the grammar for this language can be written in
[EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)
as:

```
expr = "(", expr, ")"
     | "lam", ident, expr
     | "app", expr, expr
     | literal
     | ident ;

ident   = letter, { letter | digit } ;
literal = number | bool ;
number  = digit, { digit } ;
bool    = "true" | "false" ;

letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z" ;
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

One thing that's sometimes annoying about EBNF grammars is that they can be a
bit cavalier about where whitespace goes. In our grammar, whitespace can go
anywhere there is concatenation except inside the `ident` and `number`
expressions and must separate the concatenations for the lambda abstractions
and function applications.

As you might have been able to deduce from the grammar, there are two kinds of
literals: non-negative integers, and booleans.

### Standard library

Our language has some additional values built in. They are

- `add` which adds two integers. Since functions can only take one argument in
  our language, `add` takes a number and returns a function that takes another
  number that sums both and returns the result. You use `add` to add 1 and 2
  like `app (app add 1) 2`, which evaluates to `3`.
- `gt` which compares two integers. Just like `add`, `gt` takes one number as
  an argument, returns a function that  takes another number, then returns if
  the first argument was greater than the second argument. This strategy of
  using multiple functions to handle multiple arguments one at a time is called
  [currying](https://en.wikipedia.org/wiki/Currying). You use `gt` to compare
  two numbers like `app (app gt 1) 2`, which evaluates to `false`.
- `if` which branches on a bool. Like `add` and `gt`, we'll curry the
  arguments, but here we need to take three arguments. You can use `if` like
  `app app app if false 2 3`, which evaluates to `3`.

### Your program

As input your program should take lines of expressions in the above programming
language, evaluate them fully, and output the result. The evaluation should be
"strict", meaning that your program's behavior should be identical to if it
fully evaluated the left and right hand sides of an `app` before doing the
application. All of the input expressions are syntactically valid, eventually
terminate, and the result is an integer.

### Hint

One thing you'll want to do is keep track of what variables are defined and
when. When you evaluate a lambda, you'll want to keep a snapshot of the
variables that were defined when you evaluated the lambda, so that when the
lambda is called, it knows about all of those variables still. These mappings
of variable definitions are usually called "environments" and evaluated lambdas
that are bound to an environment are usually called "closures," if you want to
Google around to read more.

### Example

#### Input

```
2
app (lam x x) 2
app lam x (x) 2
app app add 1 3
app app app if (app app gt 3 1) 10 5
```

#### Output

```
2
2
2
4
10
```

### Additional examples

These won't be tested, but just for more ideas:

#### Input

```
app app (app (lam f lam y lam x (app (app f y) x)) (lam x lam y x)) 3 4
```

#### Output

```
3
```
