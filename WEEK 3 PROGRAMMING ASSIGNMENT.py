""
Week 3 Programming Assignment
Due on 2023-02-16, 23:59 IST
Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 12 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
Define a Python function remdup(l) that takes a nonempty list of integers l and removes all duplicates in l, keeping only the last occurrence of each number. For instance:

>>> remdup([3,1,3,5])
[1, 3, 5]

>>> remdup([7,3,-1,-5])
[7, 3, -1, -5]

>>> remdup([3,5,7,5,3,7,10])
[5, 3, 7, 10]
Write a Python function splitsum(l) that takes a nonempty list of integers and returns a list [pos,neg], where pos is the sum of squares all the positive numbers in l and neg is the sum of cubes of all the negative numbers in l.

Here are some examples to show how your function should work.

>>> splitsum([1,3,-5])
[10, -125]

>>> splitsum([2,4,6])
[56, 0]

>>> splitsum([-19,-7,-6,0])
[0, -7418]

>>> splitsum([-1,2,3,-7])
[13, -344]
A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

1  2  3
4  5  6 
7  8  9
would be represented as [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

A horizonatal flip reflects each row. For instance, if we flip the previous matrix horizontally, we get

3  2  1
6  5  4 
9  8  7
which would be represented as [[3, 2, 1], [6, 5, 4], [9, 8, 7]].

A vertical flip reflects each column. For instance, if we flip the previous matrix that has already been flipped horizontally, we get

9  8  7
6  5  4 
3  2  1
which would be represented as [[9, 8, 7], [6, 5, 4], [3, 2, 1]].

Write a Python function matrixflip(m,d) that takes as input a two dimensional matrix m and a direction d, where d is either 'h' or 'v'. If d == 'h', the function should return the matrix flipped horizontally. If d == 'v', the function should retun the matrix flipped vertically. For any other value of d, the function should return m unchanged. In all cases, the argument m should remain undisturbed by the function.

Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

>>> myl = [[1,2],[3,4]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'h')
[[2, 1], [4, 3]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(myl,'v')
[[3, 4], [1, 2]]  

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(matrixflip(myl,'h'),'v')
[[4, 3], [2, 1]]

>>> myl
[[1, 2], [3, 4]]  

>>> matrixflip(matrixflip(myl,'h'),'v')
[[4, 3], [2, 1]]

>>> myl
[[1, 2], [3, 4]]


def remdup(l):
    seen = set()
    result = []
    for number in reversed(l):
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result[::-1]
def splitsum(l):
    pos = 0
    neg = 0
    for number in l:
        if number > 0:
            pos += number**2
        elif number < 0:
            neg += number**3
    return [pos, neg]
def matrixflip(m, d):
    if d == 'h':
        return [row[::-1] for row in m]
    elif d == 'v':
        return m[::-1]
    else:
        return m


