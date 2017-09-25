As the newly elected Lord Chief of the Nightmare's Observers, you've made a few changes at Castle Blink. The first, of course, was to install a complete Vivint security system! Now that you have a camera watching the tunnel through the wall, you want to implement your own motion detection algorithm to try and tell the difference between the undead, and a Nightmare's Observers ranger. With that goal in mind, you start working on your bounding box algorithm...

First, you are given three positive integer values, \\(X\\), \\(Y\\), and \\(T\\). \\(X\\) is the width of the image, \\(Y\\) is the height of the image, and \\(T\\) is your object pixel tolerance.

You are given an \\(X\\) by \\(Y\\) grid of pixels. Each pixel can have one of two values, `0` or `1`. You must find the bounding boxes for all contiguous groups of 1-pixels. Some definitions:

Object pixel tolerance
: The maximum number of steps (by [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)) between any two consecutive 1-pixels for the pixels to be considered contiguous.

A contiguous group of 1-pixels
: The largest possible set of 1-pixels such that there exists a contiguous chain of 1-pixels within the group from every 1-pixel in the group to every other 1-pixel in the group.

A contiguous chain of 1-pixels
: A sequence of 1-pixel positions such that every 1-pixel in the sequence is no more than \\(T\\) (the object pixel tolerance) pixels away (by [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry)) from the previous 1-pixel in the sequence.

There may be multiple contiguous groups in an image.

For every contiguous group of pixels, you need to output the smallest possible bounding box around that contiguous group of pixels. To describe a bounding box, you should output the top left \\(X\\) and \\(Y\\) coordinates followed by the bottom right \\(X\\) and \\(Y\\) coordinates.

In any order, you need to output the coordinates of all of the smallest possible bounding boxes around the contiguous groups of pixels.

### Example

#### Input

```
4 4 1
1 1 0 0
0 0 0 0
0 0 1 0
1 0 1 1
```

#### Output

```
0 0 1 0
2 2 3 3
0 3 0 3
```
