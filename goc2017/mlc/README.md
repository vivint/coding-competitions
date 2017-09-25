<div class="well">
  <em><strong>Editor's note:</strong> the goal of this problem is not only to
  be a fun challenge but also to teach you almost everything you need to know
  to build a neural network from scratch. If machine learning is still scary
  sounding and foreign to you, you should feel much more at ease after working
  through this problem. It's true that we left out the details of
  <a href="https://en.wikipedia.org/wiki/Backpropagation">back-propagation</a>,
  and a single-layer neural network isn't really a neural network, but in this
  problem you'll learn how to train and run a complete model! We know
  there's lots of math&mdash;don't be intimidated. If you can
  <a href="https://en.wikipedia.org/wiki/Matrix_multiplication">multiply
  matrices</a> you should be fine.</em>
</div>

A crack team of druids, having taken control of ravens and other birds, have begun flying over the northlands looking for an undead army. As the birds fly over the icy terrain, the druids sketch images of what the birds see. Your job is to take the sketches and determine if what they're seeing is the army of the dead, a group of Nightmare's Observers rangers, wild ones, or maybe just some rocks in the tundra.

To solve this problem, you're going to build and train a machine learning model... from scratch! Don't be intimidated&#8212;it will be much easier than it sounds!

### What is machine learning?

*Machine learning* is a broad and growing range of topics, but essentially
the idea is to teach the computer how to find patterns in large amounts of
data, then use those patterns to make predictions. Surprisingly, the techniques
that have been developed allow computers to translate languages, drive cars,
recognize cats, synthesize voice, understand your music tastes, cure diseases, adjust your thermostat, and even determine the difference between an undead army and rocks!

You might be surprised to learn that since about 2010, the entire artificial
intelligence and machine learning community has reorganized around a
surprisingly small and common toolbox for all of these problems. So, let's dive
in to this toolbox!

### Classification

One of the most fundamental ways of solving problems in machine learning is by
recasting problems as *classification* problems. In other words, if you can
describe a problem as data that needs labels, you can use machine learning!

Machine learning will go through a phase of *training*, where data and existing labels are provided to the system. As a motivating example, imagine you have a large collection of sketches that either depict lamprey pie or don't. Some of your sketches have already been labeled if they contain a lamprey pie or not, but the other photos we want to build a system that will automatically label them "lampreypie" or "notlampreypie." During training, we attempt to build a model of what exactly the essence of each label is. In this case, we will run all of our existing labeled sketches through the system so it can learn what makes a lamprey pie a lamprey pie.

After training, we run the unseen sketches through the model and use the model to generate classifications. If you provide a new sketch to your lampreypie/notlampreypie model, your model should be able to tell you if the sketch contains a lamprey pie, assuming your model had a good training data set and was able to capture the core concept of what a lamprey pie is.

Many different types of problems can be described as classification problems.
As an example, perhaps you want to predict which word comes next in a sequence.
Given four input words, a classifier can label those four words as "likely the
fourth word follows the last three words" or "not likely." Alternatively, the
classification label for three words could be the most likely word to follow
those three.

### How I learned to stop worrying and love multinomial logistic classification

Okay, let's do the simplest thing we can think of to take input data and
classify it.

Let's take a druid sketch, and divide it up into a 16 by 16 grid of smaller images (let's call these smaller images pixels, for no real reason in particular 😉). Now we can estimate how much each of those pixels is blackened in the sketch, and assign that to a floating-point value&#8212;the pixel value. Now what we have is a 16 by 16 pixel picture, and we're going to just put all the pixels in one big row so we have 256 pixel values in a row. So we'll say \\(\mathbf{x}\\) is a vector in 256 dimensions, and each dimension is the pixel value.

We have two labels, "lampreypie" and "notlampreypie". Just like any other machine
learning system, our system will never be 100% confident with a classification,
so we will need to output confidence probabilities. The output of our system
will be a two-dimensional vector, \\(\mathbf{p}\\). \\(p_0\\) will represent
the probability that the input should be labeled "lampreypie" and \\(p_1\\) will
represent the probability that the input should be labeled "notlampreypie."

How do we take a vector in 256 (or \\(\dim\(\mathbf{x}\)\\)) dimensions and
make something in just 2 (or \\(\dim\(\mathbf{p}\)\\)) dimensions? Why,
[matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
of course! If you have a matrix with 2 rows and 256 columns,
multiplying it by a 256-dimensional vector will result in a 2-dimensional one.

<p id="math1" class="katex-display">
<script>
katex.render(
"\\left[ \\begin{array}{cccc} "+
"W_{0,0} & W_{0,1} & \\ldots & W_{0,255} \\\\ "+
"W_{1,0} & W_{1,1} & \\ldots & W_{1,255} "+
"\\end{array} \\right] \\cdot "+
"\\left[ \\begin{array}{c} "+
"x_0 \\\\ "+
"x_1 \\\\ "+
"\\vdots \\\\ "+
"x_{255} "+
"\\end{array} \\right] = "+
"\\left[ \\begin{array}{c} "+
"? \\\\ "+
"? "+
"\\end{array} \\right]",
document.getElementById("math1"), {displayMode: true});
</script>
</p>

Surprisingly, this is actually really close to the final construction of our
classifier, but there are two problems:

 1. If one of the input \\(\mathbf{x}\\)s is all zeros, the output will have
    to be zeros. But we need one of the output dimensions to not be zero!
 2. There's nothing guaranteeing the probabilities in the output will be
    non-negative and all sum to 1.

The first problem is easy, we add a bias vector \\(\mathbf{b}\\), turning our
matrix multiplication into a standard linear equation of the form
\\(\mathbf{W}\cdot\mathbf{x}+\mathbf{b}=\mathbf{y}\\).

<p id="math2" class="katex-display">
<script>
katex.render(
"\\left[ \\begin{array}{cccc} "+
"W_{0,0} & W_{0,1} & \\ldots & W_{0,255} \\\\ "+
"W_{1,0} & W_{1,1} & \\ldots & W_{1,255} "+
"\\end{array} \\right] \\cdot "+
"\\left[ \\begin{array}{c} "+
"x_0 \\\\ "+
"x_1 \\\\ "+
"\\vdots \\\\ "+
"x_{255} "+
"\\end{array} \\right] + "+
"\\left[ \\begin{array}{c} "+
"b_0 \\\\ "+
"b_1 "+
"\\end{array} \\right] = "+
"\\left[ \\begin{array}{c} "+
"y_0 \\\\ "+
"y_1 "+
"\\end{array} \\right]",
document.getElementById("math2"), {displayMode: true});
</script>
</p>

The second problem can be solved by using the
[softmax function](https://en.wikipedia.org/wiki/Softmax_function). For a given
vector \\(\mathbf{v}\\), softmax is defined as:

<p id="math3" class="katex-display">
<script>
katex.render(
"\\text{softmax}\\left(\\mathbf{v}\\right) = \\left[ "+
"\\begin{array}{c} "+
"S\\left(v_0\\right) \\\\ "+
"S\\left(v_1\\right) \\\\ "+
"\\vdots \\\\ "+
"S\\left(v_n\\right) "+
"\\end{array} "+
"\\right], \\text{ where }"+
"S\\left(v_i\\right) = "+
"\\frac{e^{v_i}}{\\sum\\limits_{j=0}^{n-1} e^{v_j}} ",
document.getElementById("math3"), {displayMode: true});
</script>
</p>

In case the \\(\sum\\) scares you, \\(\sum_{j=0}^{n-1}\\) is basically
a math "for loop." All it's saying is that we're going to add together
everything that comes after it (\\(e^{v_j}\\)) for every \\(j\\) value from
0 to \\(n-1\\).

Softmax is a neat function! The output will be a vector where the largest
dimension in the input will be the closest number to 1, no dimensions will be
less than zero, and all dimensions sum to 1. Here are some examples:

<p id="math4" class="katex-display">
<script>
katex.render(
"\\begin{array}{l r}"+
"\\text{softmax}\\left(\\left[ \\begin{array}{c} "+
"5.4 \\\\ 1.3 "+
"\\end{array} \\right]\\right) = \\left[ \\begin{array}{c} "+
"0.983\\ldots \\\\ 0.016\\ldots "+
"\\end{array} \\right] & " +
"\\text{softmax}\\left(\\left[ \\begin{array}{c} "+
"2 \\\\ 2 "+
"\\end{array} \\right]\\right) = \\left[ \\begin{array}{c} "+
"0.5 \\\\ 0.5 "+
"\\end{array} \\right] \\end{array}" ,
document.getElementById("math4"), {displayMode: true});
</script>
</p>

Unbelievably, these are all the building blocks you need for a linear model!
Let's put all the blocks together. If you already have
\\(\mathbf{W}\cdot\mathbf{x}+\mathbf{b}=\mathbf{y}\\), your prediction
\\(\mathbf{p}\\) can be found as \\(\text{softmax}\left(\mathbf{y}\right)\\).
More fully, given an input \\(\mathbf{x}\\) and a trained model
\\(\left(\mathbf{W},\mathbf{b}\right)\\), your prediction \\(\mathbf{p}\\) is:

<p id="math5" class="katex-display">
<script>
katex.render(
"\\text{softmax}\\left(\\mathbf{W}\\cdot\\mathbf{x} + \\mathbf{b}\\right) = "+
"\\mathbf{p}",
document.getElementById("math5"), {displayMode: true});
</script>
</p>

Once again, in this context, \\(p_0\\) is the probability given the model that
the input should be labeled "lampreypie" and \\(p_1\\) is the probability given the
model that the input should be labeled "notlampreypie."

It's kind of amazing that all you need for good success with things even as
complex as handwriting recognition is a linear model such as this one.

### Scoring

How do we find \\(\mathbf{W}\\) and \\(\mathbf{b}\\)? It might surprise you but
we're going to start off by guessing some random numbers and then changing
them until we aren't predicting things too badly (via a process known as
[gradient descent](https://en.wikipedia.org/wiki/Gradient_descent)). But what
does "too badly" mean?

Recall that we have data that we've already labeled. We already have photos
labeled "lampreypie" and "notlampreypie" in what's called our *training set*. For
each photo, we're going to take whatever our current model is
(\\(\mathbf{W}\\) and \\(\mathbf{b}\\)) and find \\(\mathbf{p}\\). Perhaps
for one photo (that really is of a lamprey pie) our \\(\mathbf{p}\\) looks like
this:

<p id="math6" class="katex-display">
<script>
katex.render(
"\\begin{array}{l r}"+
"\\mathbf{p}=\\left[ \\begin{array}{c} "+
"0.4 \\\\ 0.6 "+
"\\end{array} \\right] & "+
"\\text{ the truth }=\\left[ \\begin{array}{c} "+
"1 \\\\ 0 "+
"\\end{array} \\right] \\end{array}",
document.getElementById("math6"), {displayMode: true});
</script>
</p>

This isn't great! Our model says that the photo should be labeled "notlampreypie"
with 60% probability, but it is a lamprey pie.

We need a bit more terminology. So far, we've only talked about one
sample, one label, and one prediction at a time, but obviously we have lots of
samples, lots of labels, and lots of predictions, and we want to score how our
model does not just on one sample, but on all of our training samples. Assume
we have \\(s\\) training samples, each sample has \\(d\\) dimensions, and there
are \\(l\\) labels. In the case of our 16 by 16 pixel lamprey pie photos,
\\(d = 256\\) and \\(l = 2\\). We'll refer to sample \\(i\\) as
\\(\mathbf{x}^{(i)}\\), our prediction for sample \\(i\\) as
\\(\mathbf{p}^{(i)}\\), and the correct label vector for sample \\(i\\) as
\\(\mathbf{L}^{(i)}\\). \\(\mathbf{L}^{(i)}\\) is a vector that is all zeros
except for the dimension corresponding to the correct label, where that
dimension is a 1. In other words, we have
\\(\mathbf{W}\cdot\mathbf{x}^{(i)}+\mathbf{b} = \mathbf{p}^{(i)}\\) and we want
\\(\mathbf{p}^{(i)}\\) to be as close to \\(\mathbf{L}^{(i)}\\) as possible,
for all \\(s\\) samples.

To score our model, we're going to compute something called the *average cross
entropy loss*. In general, [loss](https://en.wikipedia.org/wiki/Loss_function)
is used to mean how off the mark a machine learning model is. While there are
many ways of calculating loss, we're going to use average
[cross entropy](https://en.wikipedia.org/wiki/Cross_entropy) because it has
some nice properties.

Here's the definition of the average cross entropy loss across all samples:

<p id="math-650" class="katex-display">
<script>
katex.render(
"\\text{loss} = "+
"-\\frac{1}{s} \\cdot \\sum_{i=0}^{s-1} \\sum_{j=0}^{l-1} "+
"L_j^{(i)} \\cdot \\log \\left( p_j^{(i)} \\right)",
document.getElementById("math-650"), {displayMode: true});
</script>
</p>

All we need to do is find \\(\mathbf{W}\\) and \\(\mathbf{b}\\) that make this
loss smallest. How do we do that?

### Training

As we said before, we will start \\(\mathbf{W}\\) and \\(\mathbf{b}\\) off with
random values. For each value, choose a floating-point random number between -1
and 1.

Of course, we'll need to correct these values given the training data, and we
now have enough information to describe how we will back-propagate corrections.

The plan is to process all of the training data enough times that the loss
drops to an "acceptable level." Each time through the training data we'll
collect all of the predictions, and at the end we'll update \\(\mathbf{W}\\)
and \\(\mathbf{b}\\) with the information we've found.

One problem that can occur is that your model might overcorrect after each run.
A simple way to limit over-correction is to add a "learning rate", usually
designated \\(\alpha\\), which is some small fraction. You get to choose the
learning rate! A good default choice for \\(\alpha\\) is 0.1.

At the end of each run through all of the training data, here's how you update
\\(\mathbf{W}\\) and \\(\mathbf{b}\\):

<p id="math-700" class="katex-display">
<script>
katex.render(
"\\begin{array}{l l l} "+
"W_{m,n} & \\mathrel{-}=& \\frac{\\alpha}{s}\\cdot "+
"\\sum\\limits_{i=0}^{s-1} x_n^{(i)} \\cdot "+
"\\left( p_m^{(i)} - L_m^{(i)} \\right) "+
"\\\\\\\\ "+
"b_m & \\mathrel{-}=& \\frac{\\alpha}{s}\\cdot "+
"\\sum\\limits_{i=0}^{s-1} p_m^{(i)} - L_m^{(i)} "+
"\\end{array}",
document.getElementById("math-700"), {displayMode: true});
</script>
</p>

Just because this syntax is starting to get out of hand, let's refresh what
each symbol means.

 * \\(W_{m,n}\\) is the cell in weight matrix \\(\mathbf{W}\\) at row \\(m\\)
   and column \\(n\\).
 * \\(b_m\\) is the \\(m\\)-th dimension in the "bias" vector \\(\mathbf{b}\\).
 * \\(\alpha\\) is again your learning rate, 0.1, and \\(s\\) is how many
   training samples you have.
 * \\(x_n^{(i)}\\) is the \\(n\\)-th dimension of sample \\(i\\).
 * Likewise, \\(p_m^{(i)}\\) and \\(L_m^{(i)}\\) are the \\(m\\)-th dimensions
   of our prediction and true labels for sample \\(i\\), respectively.
   Remember that for each sample \\(i\\), \\(L_m^{(i)}\\) is zero for all but
   the dimension corresponding to the correct label, where it is 1.

If you're curious how we got these equations, we applied the
[chain rule](https://en.wikipedia.org/wiki/Chain_rule) to calculate partial
derivatives of the total loss. It's hairy, and this problem description is
already too long!

Anyway, once you've updated your \\(\mathbf{W}\\) and \\(\mathbf{b}\\), you
start the whole process over!

### When do we stop?

Knowing when to stop is a hard problem. How low your loss goes is a function
of your learning rate, how many iterations you run over your training data,
and a huge number of other factors. On the flip side, if you train your model
so your loss is too low, you run the risk of overfitting your model to your
training data, so it won't work well on data it hasn't seen before.

One of the more common ways of deciding when to
[stop training](https://en.wikipedia.org/wiki/Early_stopping) is to have a
separate validation set of samples we check our success on and stop when
we stop improving. But for this problem, to keep things simple what we're going
to do is just keep track of how our loss changes and stop when the loss stops
changing as much.

After the first 10 iterations, your loss will have changed 9 times (there was
no change from the first time since it was the first time). Take the average
of those 9 changes and stop training when your loss change is less than a
hundredth the average loss change.

### Tie it all together

Alright! If you've stuck with me this far, you've learned to implement a
multinomial logistic classifier using gradient descent,
[back-propagation](https://en.wikipedia.org/wiki/Backpropagation), and
[one-hot encoding](https://en.wikipedia.org/wiki/One-hot). Good job!

You should now be able to write a program that takes labeled training samples,
trains a model, then takes unlabeled test samples and predicts labels for them!

### Your program

As input your program should take vectors of floating-point values, followed by
a label. Some of the labels will be question marks. Your program should output
the correct label for all of the question marks it sees. The label your program
should output will always be one it has seen training examples of.

Your program will pass the tests if it labels 75% or more of the unlabeled data
correctly.

### Where to learn more

If you want to learn more or dive deeper into optimizing your solution, you
may be interested in the first section of
[Udacity's free course on Deep Learning](https://classroom.udacity.com/courses/ud730),
or [Dom Luma's tutorial on building a mini-TensorFlow](http://nbviewer.jupyter.org/github/domluna/labs/blob/master/Build%20Your%20Own%20TensorFlow.ipynb).

### Example

#### Input

```
 0.93 -1.52  1.32  0.05  1.72 undead
 1.57 -1.74  0.92 -1.33 -0.68 nightmaresobs
 0.18  1.24 -1.53  1.53  0.78 other
 1.96 -1.29 -1.50 -0.19  1.47 nightmaresobs
 1.24  0.15  0.73 -0.22  1.15 wildone
 1.41 -1.56  1.04  1.09  0.66 undead
-0.70 -0.93 -0.18  0.75  0.88 undead
 1.12 -1.45 -1.26 -0.43 -0.05 nightmaresobs
 1.89  0.21 -1.45  0.47  0.62 other
-0.60 -1.87  0.82 -0.66  1.86 nightmaresobs
-0.80 -1.99  1.74  0.65  1.46 undead
-0.03  1.35  0.11 -0.92 -0.04 wildone
-0.24 -0.03  0.58  1.32 -1.51 undead
-0.60 -0.70  1.61  0.56 -0.66 undead
 1.29 -0.39 -1.57 -0.45  1.63 nightmaresobs
 0.87  1.59 -1.61 -1.79  1.47 wildone
 1.86  1.92  0.83 -0.34  1.06 wildone
-1.09 -0.81  1.47  1.82  0.06 undead
-0.99 -1.00 -1.45 -1.02 -1.06 nightmaresobs
-0.82 -0.56  0.82  0.79 -1.02 undead
-1.86  0.77 -0.58  0.82 -1.94 other
 0.15  1.18 -0.87  0.78  2.00 other
 1.18  0.79  1.08 -1.65 -0.73 wildone
 0.37  1.78  0.01  0.06 -0.50 other
-0.35  0.31  1.18 -1.83 -0.57 wildone
 0.91  1.14 -1.85  0.39  0.07 other
-1.61  0.28 -0.31  0.93  0.77 other
-0.11 -1.75 -1.66 -1.55 -0.79 nightmaresobs
 0.05  1.03 -0.23  1.49  1.66 other
-1.99  0.43 -0.99  1.72  0.52 other
-0.30  0.40 -0.70  0.51  0.07 other
-0.54  1.92 -1.13 -1.53  1.73 wildone
-0.52  0.44 -0.84 -0.11  0.10 wildone
-1.00 -1.82 -1.19 -0.67 -1.18 nightmaresobs
-1.81  0.10 -1.64 -1.47 -1.86 wildone
-1.77  0.53 -1.28  0.55 -1.15 other
 0.29 -0.28 -0.41  0.70  1.80 undead
-0.91  0.02  1.60 -1.44 -1.89 wildone
 1.24 -0.42 -1.30 -0.80 -0.54 nightmaresobs
-1.98 -1.15  0.54 -0.14 -1.24 nightmaresobs
 1.26 -1.02 -1.08 -1.27  1.65 ?
 1.97  1.14  0.51  0.96 -0.36 ?
 0.99  0.14 -0.97 -1.90 -0.87 ?
 1.54 -1.83  1.59  1.98 -0.41 ?
-1.81  0.34 -0.83  0.90 -1.60 ?
```

#### Output

```
nightmaresobs
other
wildone
undead
other
```
