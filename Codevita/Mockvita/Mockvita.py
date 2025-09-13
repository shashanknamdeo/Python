"""
Frankenstein
Problem Description
"Muahahaha! No one can stop me from creating the elixir of life," -Frankenstein. Frankenstein is an alchemist who is always striving to craft the elixir of life.

The elixir of life grants immortality to whoever drinks it. In his attempts to brew the elixir of life, Frankenstein combines numerous ingredients and potions, believing he will eventually succeed. However, he has never succeeded thus far.

But each time he brews something, he meticulously notes the ingredients. For example, when he combined snake fangs and wolfsbane, he discovered the awakening potion. In his notes, he recorded the recipe as follows:

awakening = snakefangs + wolfbane

Similarly, when three ingredients were required, he noted the recipe in his notes as

thunderstorm = rain + wind + lightening

In general, the recipe would be

Potion 1 = Ingredient 1 + Ingredient 2

Potion 2 = Ingredient 1 + Ingredient 2 + Ingredient 3

Potion 3 = Ingredient 1 + Ingredient 2 + Ingredient 3 + Ingredient 4

and so on ...

Every brew requires magical orbs, which are mythical energy balls. The number of magical orbs needed for a recipe is equal to the number of ingredients minus one.

A recipe of a potion includes multiple ingredients. An ingredient can be an item or a potion. Items are readily available things and while potions are brewed from items. In his notes, the resultant is always a potion.

He observed that sometimes the same potion can be created using different recipes, with some requiring fewer magical orbs. Given a potion and his notes, determine the minimum number of magical orbs needed to create that potion.

Constraints
0 < N < 20

Input
First line contains an integer N representing the number of recipes he noted.

Next N lines contain string without space representing the recipes in his notes as mentioned above.

Last line contains a single string representing the potion that he needs to brew.

Output
Print single integer representing the minimum number of magical orbs required.

Time Limit (secs)
1

Examples
Example1

Input

4

awakening=snakefangs+wolfbane

veritaserum=snakefangs+awakening

dragontonic=snakefangs+velarin

dragontonic=awakening+veritaserum

dragontonic

Output

1

Explanation

Based on the input, we need to determine the minimum number of magical orbs required to brew dragontonic. According to the notes, there are two recipes available for brewing dragontonic.

The two ways of brewing dragontonic are, dragontonic=awakening+veritaserum and dragontonic=snakefangs+velarin

The recipe with awakening, veritaserum where awakening is a potion that must be brewed first. Brewing awakening requires 1 magical orb and brewing it with veritaserum requires one additional magical orb, totaling 2 magical orbs.

Since second recipe of dragontonic requires only 1 magical orb which is the minimum number of orbs required, hence print 1 as output.

Example 2

Input

6

oculus=thunderbrew+jellfish

felix=thunderbrew+pumpkin

wigenweld=thunderbrew+ladybug

wigenweld=oculus+felix

thunderbrew=pumpkin+firefly

maxima=pumpkin+ladybug

wigenweld

Output

2

Explanation

To brew wigenweld with the minimum number of orbs, he first brewed thunderbrew, which requires 1 orb. Then, brewing thunderbrew with ladybug required an additional orb, resulting in wigenweld. Therefore, a total of 2 orbs were needed, which is the minimum requirement, hence the output is 2.
"""


"""
CountTheShapes
Problem Description
In today's class, little Aadhya learned about closed figures, allowing her to differentiate between shapes that are closed and those that are not.

She was tasked with identifying closed shapes formed from a given set of line segments. Feeling a bit confused, she has sought your help. Given a set of line segments that only intersect at their endpoints, determine the total number of closed figures formed. Note that there exist some line segments that do not intersect at all.

Note: No more than 2 lines will intersect at a point.

Constraints
1 <= N <= 1000

0 <= x, y <= 100

Input
First line consists of an integer N, denoting the number of line segments.

The following N lines each contain 4 space-separated integers that represent the starting and ending points of a line segment in the format x1 y1 x2 y2.

Output
Print a single integer denoting the number of closed figured formed by the given set of line segments.

Time Limit (secs)
1

Examples
Example 1

Input

15

0 0 1 0

3 1 3 3

3 3 1 3

5 3 4 3

5 4 6 4

1 0 0 1

0 1 0 0

1 1 3 1

6 4 6 3

1 3 1 1

4 1 5 1

6 3 6 2

5 1 5 3

3 0 4 0

4 3 4 1

Output

3

Explanation

The given lines when represented in a 2D plane looks like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@1a78dacd:image1.png

As we can see here there are 3 closed figures, hence print 3.

Example 2

Input

15

0 0 6 0

6 0 6 6

6 6 0 6

0 6 0 0

1 1 3 1

3 1 3 4

3 4 1 4

1 4 1 1

4 4 5 4

5 4 5 5

5 5 4 5

4 5 4 4

0 7 6 7

6 7 3 9

3 9 0 7

Output

4

Explanation

The given lines when represented in a 2D plane looks like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@1a78dacd:image2.png

As we can see here there are 4 closed figures, hence print 4.

Example 3

Input

14

2 1 2 0

0 6 6 3

0 3 5 3

5 3 5 0

1 2 1 0

1 0 0 0

0 0 0 3

2 0 3 0

3 0 3 1

3 1 2 1

5 0 4 0

4 0 4 2

4 2 1 2

0 4 5 4

Output

2

Explanation

The given lines when represented in a 2D plane looks like below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@1a78dacd:image3.png

As we can see here there are 2 closed figures, hence print 2.
"""



"""
MirrorMaze
Problem Description
In the mysterious island named Reflectia, there's a grid made up of M rows and N columns. Some cells in this grid are empty, while others hold mirrors which are placed diagonally to the cells. These mirrors are the reason why the island is called Reflectia - they bounce light beams in the opposite direction when the light hits them. The mirrors are placed in two ways viz. slanted forward (/) or slanted backwards (\).

Rohit, a curious young explorer, decided to explore the Matrix with a flashlight in his hand as the island is very dark and is rumoured to be haunted. Once he entered, he aimed to find out the maximum number of cells the light could travel to, making a closed loop, within the grid when it is bounced on one of the mirrors in the grid. As it was too dark, he noted the structure of the grid and came out.

Given the structure of the grid that Rohit noted, find out what's the maximum number of cells the light could travel to, making a closed loop [a closed polygon shape], within the grid when it is bounced on one of the mirrors in the grid.

Constraints
3 < M, N < 50

Input
First line contains two integers separated by space, representing M and N.

Next M Lines contains N space separated characters viz. {'/', '\', '0'} representing the grid structure.

Output
Single integer representing the maximum number of cells that can be covered in the loop formed by the reflected light beam.

Time Limit (secs)
1

Examples
Example 1

Input

5 5

/ / 0 0 \

0 0 0 / 0

0 \ 0 0 /

\ / \ / 0

0 0 \ \ \

Output

10

Explanation

The below diagram depicts the input.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@bc57b40:image1.png

The mirror at indices [1,2], [1,5], [3,2] and [3,5] can form a loop covering 10 cells, which is the maximum possible.

Example 2

Input

6 6

0 0 0 0 / \

/ 0 / 0 / 0

0 \ 0 \ / 0

0 / \ \ / 0

0 / \ / 0 0

0 0 / \ 0 /

Output

0

Explanation

The below diagram depicts the input.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@bc57b40:image2.png

We cannot form any loop inside the given grid. Hence, print 0.
"""


"""
FaultySegment
Problem Description
Gagan, along with his friend, recently launched a small firm that manufactures basic calculators, which use seven-segment displays to show results.

One day, an employee brought a faulty calculator to Gagan, reporting that it was giving incorrect results due to a software glitch. After analysing its behaviour, Gagan discovered that it wasn't a software issue but rather a flaw in the 7-segment display, where one of the LEDs was malfunctioning.

So, Gagan thought of finding the LED which is malfunctioning.

The calculator only has buttons for the digits 0-9 and the symbols +, -, %, =, and *. When clicked, these buttons will display their respective symbols as a seven-segment display, represented by a 3x3 matrix.

The arrangement of 7 segment display for each number from 0-9 and for the five mathematical operators is shown below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@547e29a4:image1.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@547e29a4:image2.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@547e29a4:image3.png

Given the equation that Gagan typed and the current display on the calculator, determine which character corresponds to the LED that should be toggled to make the equation correct.

Note: Solve the equation sequentially from left to right, without considering the precedence of operators.

Constraints
5 <= N <= 30

It is guaranteed that RHS or the equal to symbol will not be faulty.

RHS will not have any operators.

It is guaranteed that all the testcases will have only one solution.

Input
First line consists of N denoting the number of characters in the given equation.

Next 3 lines will have the 7-segment display of the equation which Gagan typed.

Output
Print the position corresponding to the faulty character displayed. Count starts from one.

Time Limit (secs)
1

Examples
Example 1

Input

5

       _     _ 
  ||_  _| _ |_|
  ||  |_  _  _|

Output

1

Explanation

After processing each character (represented as a 3x3 matrix), we get the equation 1+2 = 9, which is incorrect. To correct it, we need to toggle one LED in the first character (1) to make it 7, resulting in the correct equation 7+2 = 9. Since the error is in the first character, print 1.

Example 2

Input

6

 _     _          
 _||_  _| _   |  |
|_ |   _| _   |  |

Output

3

Explanation

After processing each character (represented as a 3x3 matrix), we get the equation 2+3=11, which is incorrect. To correct it, we need to toggle one LED in the third character (3) to make it 9, resulting in the correct equation 2+9=11. Since the error is in the third character, print 3.
"""

"""

Magic Stars Intensity
Problem Description
In the 1930s, King Krishnadevaraya, who had a great love for magic, kept a personal magician in his palace. Whenever he desired to witness a magical performance, he would command the magician to entertain him with his craft.

The magician constantly aimed to impress the king with new magical tricks. One day, he cast magical lines across the vast expanse of the palace floor, which was covered in tiles. Each tile is a square with sides of 1 unit length; thus, you can say the palace floor resembles a 2d plane.

Since these are magical lines, when they are drawn, they only align with the edges of the tiles or pass through their corners.

When these magical lines intersect, they create points of light called n-stars, where n ranges from 2 to 8. Each n-star forms when n lines intersect, and all these stars generate light.

For calculating the intensity of the star, there exist two cases which are explained below.

Consider below cases carefully.

Case 1 - The line is only one side to the star i.e., the star won't cut the line into two parts.

Consider the lines (4, 4, 4, 2), (4, 4, 7, 7) and (4, 4, 3, 5). These lines are intersecting at the point (4, 4). Since three lines intersect at a point, they form a star known as a 3-star.

Now, the intensity of the star = minimum (the number of cells these 3 lines are touching from the point of star formation to the last) = minimum (2, 3, 1) = 1

So, the intensity of this star will be 1.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6f6a7463:image1.png

Case 2 - The line is two sides to the star i.e., the star cuts the line into two parts.

Consider the lines (3, 3, 7, 7), (3, 5, 6,2) and (4, 2, 4, 6). These lines are intersecting at the point (4, 4). Since three lines intersect at a point, they form a star known as a 3-star.

In this case, the intensity of the star = minimum (the number of cells these 3 lines are touching from the point of star formation to the last on both sides) = minimum (1, 1, 2, 2, 3, 2) = 1

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6f6a7463:image2.png

Given N lines and the type of star for which you need to determine the intensity, calculate the intensity for all such stars according to the cases described and print their total sum. If no stars of the specified type are present, print 0.

Constraints
1 <= N <= 50

2 <= K <= 8

0 <= x, y <= 100

Lines will not overlap either partially or completely.

Input
First line consists of an integer N, denoting the number of magical lines the magician casted.

The next N lines contain four space-separated integers each, representing the x and y coordinates of the starting and ending points of the magical lines.

The last line consists of an integer K denoting the type of star for which you need to calculate the intensity.

Output
Print a single integer representing the total intensity of all stars of the specified type given in the input. If no such stars are present, print 0.

Time Limit (secs)
1

Examples
Example 1

Input

7

4 2 4 6

6 5 6 7

1 3 3 5

3 5 4 4

3 3 7 7

2 2 2 5

4 4 5 3

4

Output

1

Explanation

The lines given in the above input are represented in the below figure.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6f6a7463:image3.png

Here, the star formed at (4, 4) is a 4-star because it is created by 4 lines. According to given cases, the intensity of this star is minimum (2, 1, 1, 2, 1, 3), resulting in an intensity of 1. Since there is only one 4-star, the output is 1.

Example 2

Input

5

1 1 8 8

3 1 3 4

5 1 5 8

1 3 3 3

7 2 7 9

2

Output

4

Explanation

The lines given in the above input are represented in the below figure.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6f6a7463:image4.png

There are two 2-stars formed at the positions (5, 5) and (7, 7). The intensity of star at (5, 5) is minimum (4, 3, 3, 4) which is 3 and the intensity of star at (7, 7) is minimum (1, 2, 6, 5) which is 1. So, the total intensity of all 2-stars will be 3+1 = 4.

"""


"""
ReenuCircuit
Problem Description
Reenu is an electrical engineer who frequently designs new circuits. She constructs circuits using two types of resistors: horizontal and vertical, along with a junction. In each circuit, there are two positions: an opening and a closing. The circuit is connected to the power supply at the opening position, and the current flows through the resistors and junctions until it reaches the closing position.

In the matrix representation of the circuit, power can only flow vertically (up or down) if a vertical resistor is present, and it can only flow horizontally (left or right) if a horizontal resistor is present. The junction connects all four sides. The vertical and horizontal resistors have 1 units of resistance, while the junction considered to be having low resistance, ignorable.

Vertical resistor is represented by "|" (pipe), horizontal represented by "-"(hyphen) .a "." (period) symbol represents terminals and "+" (plus) representing junction.


The resistance for series connection is RT = R1 + R2 and for parallel connection is 1/RT = 1/R1 + 1/R2.To know about resistance in series and parallel look here.

Given the circuit, reduce and determine the equal resistance of the circuit between opening position and closing position.

To know more about reduction of resistor in series and parallel look here

Constraints
3 <= N <= 10

Input
First line consists of N, denoting the number of rows, columns in the matrix.

The following N lines represent the circuit as a matrix.

Output
Print the total resistance of the circuit.

Time Limit (secs)
1

Examples
Example 1

Input

4
.-+-
--|-
+-+-
|-+.

Output

2

Explanation

The above input is visualized below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image1.png

The Equivalent circuit of this will be,

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image2.png

Two resistors in series and adding them results in 2 units of resistors which is the equivalent.

Example 2

Input

5
.-+-+
--|-|
--|-|
--|-|
--+-.

Output

3

Explanation

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image3.png

The equivalent circuits look as below.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image4.png

The reduction goes as below...

First the three resistors series on both the branches will combined together.Followed by 3 and 1 unit resistors on both the branches will combined together.Forming 4 unit of resitors in parallel.The 4 units of resistors are combined and become a single 2 units of resistors

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image5.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image6.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@24f43aa3:image7.png

The resultant 2 units of resistor is series with 1 unit of resistor equivalent to 3 units of resistors.And thus the equivalent resistor 3.
"""