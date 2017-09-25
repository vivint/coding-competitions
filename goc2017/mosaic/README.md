Rabbithutch is the largest castle ever built in Vivinteros. It stands as a symbol of magnificence and grandeur. Or at least it did, until Eyegone the Conquistador flew right over its grand walls with his dragon Noirelab, and turned it into a flaming pile of half-melted rocks. So it goes.

Masons from all over the kingdom were called in to fix Rabbithutch's renowned entryway mosaics, but you put in the lowest bid and now the job is yours! Congratulations.

Rabbithutch's entryway mosaics are pretty special. Instead of traditional thin tiles, these mosaics were made with brick cubes. Each brick cube was in turn composed of twenty-seven smaller bricks. This means that when you look at the side of a brick cube, what you're seeing are the faces of nine different colored bricks.  Somehow, you have to reassemble all the bricks into cubes to restore the entryway's mosaic to its former glory.

Due to the dragon fire, melee combat, and what not else, bricks lay strewn all over. So the trick is going to be identifying which colored bricks will make the design again.

### The sections

Luckily, you've managed to find the original builder's plans for the entryway. She was a meticulous planner and diagrammed each and every brick cube before actually building it. She explained that each brick cube is simply a 3x3x3 arrangement of colored bricks. Bricks occur in any of eight colors: red, blue, green, yellow, magenta, orange, cyan, and white. Each color is indicated in the plans by the first letter of its name.

Below you'll find the original builder's description of a brick cube and a matching diagram to the right:

<div style="float: right;">
  <img src="/static/images/castle-brick.png">
</div>

```
OGW CMC YGY
WMG BWM ROR
BRY MGO CWB
```

She points out that this is the top face:

```
OGW ___ ___
WMG ___ ___
BRY ___ ___
```

and that this is the front face:

```
___ ___ ___
___ ___ ___
BRY MGO CWB
```

and that this is the side face:

```
__W __C __Y
__G __M __R
__Y __O __B
```

Once again the full brick cube is:

```
OGW CMC YGY
WMG BWM ROR
BRY MGO CWB
```

The left-most collection of nine is the top row and the right-most collection of
nine is the bottom row. This is how she describes a full brick cube.

### The entryway

![entryway](/static/images/castle-tiles.jpg)

The entryway is a collection of these brick cubes set into the floor. You can only see one side of the bricks!

The original builder's plans are laid out as a two-dimensional blueprint. One area might look like this:

```
YYCRBCYYMWMYCGYMGBRYYGRGWGRGRGOBGGCCMRWWOGWWC
BYMMGWRRCROCMMCCOGGCWWGMYGGGRBWCCYYGBRWBMBCWW
MRYGBYGCWYOGMRGYOOMGGOMRYOYWOYMCCYRROBWGCGMOW
GRGOOBCRBGYGRGMBBMWYGMGYWMWGOYYYOBOWYCWOMRBGB
WCOBOWYYYGWBGYOBMYRYGBYBYWGOWGGBGOCWBBGBCORMO
GCWOYCMBGMOWWRGOOYCOGRYGCOOWWCBYYGWYCBOBGOWCC
COORCMRROWRYGYWWGYYOGMGGGWGOWWYBGYOMMOBCOCBBR
YBBGWYBYBGBGMOOMRMRBWMBRWGRCWYWCRMCRBRYGGGOYG
YOBRRYRYRCBYWROCMYMOOYGOYCRYROWOOBCGYCBRBRBWB
```

Here is the same blueprint with the visible faces of the bricks separated:

```
YYC RBC YYM WMY CGY MGB RYY GRG WGR GRG OBG GCC MRW WOG WWC
BYM MGW RRC ROC MMC COG GCW WGM YGG GRB WCC YYG BRW BMB CWW
MRY GBY GCW YOG MRG YOO MGG OMR YOY WOY MCC YRR OBW GCG MOW

GRG OOB CRB GYG RGM BBM WYG MGY WMW GOY YYO BOW YCW OMR BGB
WCO BOW YYY GWB GYO BMY RYG BYB YWG OWG GBG OCW BBG BCO RMO
GCW OYC MBG MOW WRG OOY COG RYG COO WWC BYY GWY CBO BGO WCC

COO RCM RRO WRY GYW WGY YOG MGG GWG OWW YBG YOM MOB COC BBR
YBB GWY BYB GBG MOO MRM RBW MBR WGR CWY WCR MCR BRY GGG OYG
YOB RRY RYR CBY WRO CMY MOO YGO YCR YRO WOO BCG YCB RBR BWB
```

Each of these bricks is just one face of a 3x3x3 brick cube. There are forty-five brick cubes represented here, and there are eighteen other colors for each of these brick cubes you can't see!

### Instructions

First, you'll be given three numbers, \\(h\\), \\(v\\), and \\(n\\). The first number, \\(h\\), is the horizontal length of your entryway in brick cubes, the second number, \\(v\\), is the vertical length of your entryway in brick cubes, and the third number, \\(n\\), is how many brick cube descriptions you'll receive.

Next you'll receive a description of one section of the entryway. It will be \\(h\\) by \\(v\\) brick cubes in size.

Last, you'll receive \\(n\\) brick cube descriptions.

For each brick cube you receive, you need to output the maximum number of copies of that brick you could use in this section of the entryway, assuming bricks are always aligned in a grid (a brick is never offset by a third of a brick).

### Example

#### Input

```
15 3 2

YYCRBCYYMWMYCGYMGBRYYGRGWGRGRGOBGGCCMRWWOGWWC
BYMMGWRRCROCMMCCOGGCWWGMYGGGRBWCCYYGBRWBMBCWW
MRYGBYGCWYOGMRGYOOMGGOMRYOYWOYMCCYRROBWGCGMOW
GRGOOBCRBGYGRGMBBMWYGMGYWMWGOYYYOBOWYCWOMRBGB
WCOBOWYYYGWBGYOBMYRYGBYBYWGOWGGBGOCWBBGBCORMO
GCWOYCMBGMOWWRGOOYCOGRYGCOOWWCBYYGWYCBOBGOWCC
COORCMRROWRYGYWWGYYOGMGGGWGOWWYBGYOMMOBCOCBBR
YBBGWYBYBGBGMOOMRMRBWMBRWGRCWYWCRMCRBRYGGGOYG
YOBRRYRYRCBYWROCMYMOOYGOYCRYROWOOBCGYCBRBRBWB

CGM OGR CGW
WYB YYR CGW
OWO WGB WMW

RBC WCM MCR
MGW MWO YWG
GBY OBB YRR
```

#### Output

```
1
2
```
