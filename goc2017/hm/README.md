<div class="well">
  <em><p><strong>Editor's note:</strong> recently we were surprised to discover
  just how few concise, easy to understand descriptions of the overall basics
  of <a href="https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system">Hindley-Milner
  type inference</a> actually exist. If you haven't heard of Hindley-Milner
  type inference, basically it's how Haskell is able to figure out what type
  all your variables are without requiring you to specify them everywhere. Many
  descriptions assume
  quite a bit of background in
  <a href="http://www.cs.cornell.edu/~ross/publications/mixedsite/tutorial.html">type-inference
  formalism</a> off the bat, which isn't very accessible.</p>
  <p>So, we wrote a nice outline and turned it into a programming contest
  problem. The goal of this problem is not only to
  be fun but also to teach you almost everything you need to know
  to implement Hindley-Milner type inference! You don't even need to know
  functional programming. This problem is easily solved with Python. To keep
  this in scope for a programming contest, we skipped explaining
  <a href="https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system#Let-polymorphism">let-polymorphism</a>,
  but this problem, combined with the previous <a href="/problems/laminterp">interpreter
  problem</a>, should lead to quite a bit of insight about how typed programming
  languages are created.</p></em>
</div>

You've discovered an ancient system of symbols, dating back to the Kids in the Woods. Having [written an interpreter](/problems/laminterp) for the language, you've noticed that expressions have certain types, and that different types have different meanings. It would be useful if for any given expression, you could discern its type.

In this problem, you're going to build type inference for a simple functional
programming language.

### Type inference for what programming language?

The programming language you will be applying types to is very simple: there
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

### What types am I inferring?

Expressions in this language can be given types. There are three main type
categories:

- The literal types `int` for integer values and `bool` for boolean values.
- Type variables, like `a` or `b` that can stand in for any type.
- The lambda type `lam a b`.

For example, the identity function that just returns its input, `lam x x`,
has type `lam a a`. Applying the identity function to an integer,
`app (lam x x) 2`, would have type `int`, and applying it to a bool,
`app (lam x x) true`, would have type `bool`. Thus, the `a` in `lam a a` stood
in for both `int` and `bool`.

A grammar for the types can be written as:

```
type = "(", type, ")"
     | "int" | "bool"
     | "lam", type, type
     | ident ;
```

### Standard library

Our language has some additional values built in. They are

- `add` with type `lam int (lam int int)` which adds two integers. Since
  functions can only take one argument in our language, `add` takes a number
  and returns a function that takes another number that sums both and returns
  the result. You use `add` to add 1 and 2 like `app (app add 1) 2`.
- `gt` with type `lam int (lam int bool)` which compares two integers. Just
  like `add`, `gt` takes one number as an argument, returns a function that
  takes another number, then returns if the first argument was greater than
  the second argument. This strategy of using multiple functions to handle
  multiple arguments one at a time is called
  [currying](https://en.wikipedia.org/wiki/Currying).
- `if` with type `lam bool (lam a (lam a a))` which branches on a bool. Like
  `add` and `gt`, we'll curry the arguments, but here we need to take three
  arguments. Ultimately `if` will return the same value type that either `if`
  branch would have been. Perhaps `a` itself is a function type representing
  more code.
- `fix` with type `lam (lam a a) a` which is the fixed point combinator. `fix`
  is used to provide recursion to our language. Without it, the well typed
  expressions would not be Turing complete! If you're interested in reading
  more about how a fixed point combinator even does this, you might be
  interested in reading about [how to implement "fizz buzz" in an untyped
  version of this language](http://www.jtolds.com/writing/2017/03/whiteboard-problems-in-pure-lambda-calculus/), but you won't need to understand how for this problem.

### How does type inference work?

Once you have parsed the input expression into an
[abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree),
type inference should proceed in two phases, **constraint generation** and
**solving**.

#### Constraint generation

Constraints define an equivalence between two types. For example, we could have
a list of constraints like

```
a         = lam int int
lam int c = lam b int
a         = c
```

Constraint generation is an algorithm that takes as input an environment (a
mapping of name to type--you'll put the standard library in here) and the
AST, and should output the type of the AST and a list of constraints. The type
that is output is not necessarily the final type of the expression. For example,
it could output the type `c` with the list of constraints above. Just returning
`c` as the final type of the expression without the associated list of
constraints would be too general.

Here's a sketch of how constraint generation should work:

- If the node is an `int` or `bool`, return the associated type (just `int`
  or `bool`) and no constraints.
- If the node is an identifier, look it up in the type environment and return
  that type with no constraints.
- If the node is a `lam arg body`, generate a new type variable `type_var` and
  insert it into the environment using the lambda argument `arg` as the key.
  Then calculate the type and constraints for the body, and return a
  `lam type_var body_type` with those constraints. Be sure to clean up `arg`
  from the environment before you return.
- If the node is an `app left right`, then calculate the types and constraints
  for the left and right sides of the application. Generate a new type variable
  `type_var` and append the constraint that the left type must be a
  `lam right_type type_var`. Return the type variable and all of the
  constraints.

For example, the type and list of constraints for the expression (notice that
parentheses aren't needed for this to be unambiguous, even if they make it
easier to read)

```
lam x (app (app add 2) x)
```

would be

```
type:        lam a0 a2
constraints: a1                    = lam a0 a2
             lam int (lam int int) = lam int a1
```

#### Solving

The main goal of solving is determining a substitution that will take our type
from constraint generation and mapping it to the output type. So, first, you
will need to be able to perform substitutions. Second, you will need to use the
constraints to determine the substitution.

A substitution should just map type variables to other types, and applying a
substitution on to a type should replace all occurrences of the substituted
variables, returning a new type. A substitution is made up of multiple
individual rules. An example substitution rule might look like:

```
  a => lam int c
```

##### Combining substitutions

It will be important to be able to combine substitutions. When
combining, you should apply the "left" substitution on to the "right"
substitution, and then overwrite all values from the "right" substitution on to
the "left". For example, if we had the substitutions

```
left:
  a => lam int c
  b => int

right:
  d => lam a int
  b => bool
```

then combining them as `combine(left, right)` would output

```
combine(left, right):
  a => lam int c
  b => bool
  d => lam (lam int c) int
```

Note that for this `combine` operation, you don't need to worry about
symmetrically applying the "right" substitution on to the "left" one. If the
"right" set had a definition for `c`, it would just end up in the output
result, along with the definitions of `a` and `d` that use `c`.

##### Unification

Unification is the process that will allow us to build up the final
substitution for our solver. The algorithm takes as input two types and returns
a substitution such that if it were applied to the first type, the output would
be the second type. Since the type syntax also forms a tree, we will use a
similar recursive definition like we did in constraint generation.

Here's a sketch of what we will do to the type pair constraints constraint
generation gave us:

- If the first type is equal to the second type, return an empty substitution.
- If the first and second type are both lambdas,
  - Unify the arguments to get the argument substitution
  - Apply the argument substitution to the bodies and unify those to get a body
    substitution.
  - return combine(body substitution, argument substitution)
- If either argument is a type variable, return a substitution from the
  variable name to the other type.

##### Solving

To generate the final substitution, loop over the list of constraints. For
each constraint, unify the two types to get a substitution. The goal is to
remove as many type variables as possible, so apply that substitution to the
remainder of the constraints (both the left and right side of the equality),
and fold it in to your final substitution by

```
final = combine(sub, final)
```

When you have run out of constraints, return your final substitution. Apply
that final substitution to the type returned by constraint generation to get
the final type.

### Your program

As input your program should take lines of expressions in the above programming
language, and output the most general type for those expressions as explained
above. All of the input expressions are syntactically valid and well typed.
The output does not need to use any specific type variables or parenthesis.
For example, if  `lam a (lam b b)` would be accepted, so would
`(lam Z lam FOO (FOO))`.

In case you didn't notice, you just implemented most of the
[Hindley-Milner](https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system)
type-inference algorithm! Add [let-polymorphism](https://en.wikipedia.org/wiki/Hindley%E2%80%93Milner_type_system#Let-polymorphism) and you have the full thing!

### Example

#### Input

```
2
true
lam x x
app (lam x x) 2
app lam x (x) 2
add
```

#### Output

```
int
bool
lam a a
int
int
lam int (lam int int)
```
