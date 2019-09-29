"""
Week 8 Programming Assignment
Due on 2019-09-27, 23:59 IST
For this assignment, you have to write a complete Python program. Paste your code in the window below.

You may define additional auxiliary functions as needed.
There are some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases
"Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
Domino Solitaire
(Indian National Olympiad in Informatics, 2008)

In Domino Solitaire, you have a grid with two rows and many columns. Each square in the grid contains an integer. You are given a supply of rectangular 2 × 1 tiles, each of which exactly covers two adjacent squares of the grid. You have to place tiles to cover all the squares in the grid such that each tile covers two squares and no pair of tiles overlap.

The score for a tile is the difference between the bigger and the smaller number that are covered by the tile. The aim of the game is to maximize the sum of the scores of all the tiles.

Here is an example of a grid, along with two different tilings and their scores.


The score for Tiling 1 is 12 = (9−8)+(6−2)+(7−1)+(3−2) while the score for Tiling 2 is 6 = (8−6)+(9−7)+(3−2)+(2−1). There are other tilings possible for this grid, but you can check that Tiling 1 has the maximum score among all tilings.

Your task is to read the grid of numbers and compute the maximum score that can be achieved by any tiling of the grid.

Solution hint
Recursively find the best tiling, from left to right. You can start the tiling with one vertical tile or two horizontal tiles. Use dynamic programming to evaluate the recursive expression efficiently.

Input format
The first line contains one integer N, the number of columns in the grid. This is followed by 2 lines describing the grid. Each of these lines consists of N integers, separated by blanks.

Output format
A single integer indicating the maximum score that can be achieved by any tiling of the given grid.

Test Data:
For all inputs, 1 ≤ N ≤ 105. Each integer in the grid is in the range {0,1,...,104}.

Sample Input:
4
8 6 2 3
9 7 1 2
Sample Output:
12
"""

n = int(input())
arr = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))

prev_state = 0
final = abs(arr[0]-arr_2[0]) #initial conditions
for i in range(1,n):
	vertical_place = final + abs(arr[i]-arr_2[i])
	horizontal_place = prev_state + abs(arr[i] - arr[i-1]) + abs(arr_2[i] - arr_2[i-1])
	prev_state = final 
	final = max(vertical_place,horizontal_place)
print(final)