""
Week 3 Programming Assignment
Due on 2019-08-22, 23:59 IST
Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.

You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.

Here are some examples of how your function should work.

  >>> expanding([1,3,7,2,9])
  True
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 9-2 = 7.

  >>> expanding([1,3,7,2,-3]) 
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 7-2 = 5, 2-(-3) = 5, so not strictly increasing.

  >>> expanding([1,3,7,10])
  False
Explanation: Differences between adjacent elements are 3-1 = 2, 7-3 = 4, 10-7 = 3, so not (strictly) increasing.

Write a function accordian(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements alternates between increasing strictly and decreasing strictly.

Here are some examples of how your function should work.

 
  >>> accordian([1,5,1])
  False
Explanation: Differences between adjacent elements are 5-1 = 4, 5-1 = 4, which are equal.

 
  >>> accordian([1,5,2,8,3])
  True
Explanation: Differences between adjacent elements are 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences decrease, increase and then decrease.

 
  >>> accordian([-2,1,5,2,8,3]) 
  True
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-3 = 5, so the differences increase, decrease, increase and then decrease.

 
  >>> accordian([1,5,2,8,1])
  False
Explanation: Differences between adjacent elements are 1-(-2) = 3, 5-1 = 4, 5-2 = 3, 8-2 = 6, 8-1 = 7, so the differences increase, decrease, increase and then increase again.

A square n×n matrix of integers can be written in Python as a list with n elements, where each element is in turn a list of n integers, representing a row of the matrix. For instance, the matrix

  1  2  3
  4  5  6
  7  8  9
would be represented as [[1,2,3], [4,5,6], [7,8,9]].

Write a function rotate(m) that takes a list representation m of a square matrix as input, and returns the matrix obtained by rotating the original matrix clockwize by 90 degrees. For instance, if we rotate the matrix above, we get

  7  4  1
  8  5  2
  9  6  3
Your function should not modify the argument m provided to the function rotate().

Here are some examples of how your function should work.

 
  >>> rotate([[1,2],[3,4]])
  [[3, 1], [4, 2]]
Explanation:

     1  2    becomes     3  1
     3  4                4  2
  
 
  >>> rotate([[1,2,3],[4,5,6],[7,8,9]])
  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Explanation:

     1  2  3    becomes   7  4  1
     4  5  6              8  5  2
     7  8  9              9  6  3
  
  >>> rotate([[1,1,1],[2,2,2],[3,3,3]])
  [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
Explanation:

     1  1  1    becomes   3  2  1
     2  2  2              3  2  1
     3  3  3              3  2  1
  

""

#SOLUTION

def expanding(l):
    a=0
    for i in range(1,len(l)):
        if a >= abs(l[i]-l[i-1]):
            return False
        a=abs(l[i]-l[i-1])
    else:
        return True
      
def accordian(l):
    if len(l)<3:
        return False
    new=[]
    for q in range(len(l)-1):
        k=abs(l[q]-l[q+1])
        new.append(k)
    tep=[]
    for i in range(0,len(new)-1):
        if new[i]>new[i+1]:
            tep.append("L")
        if new[i]<new[i+1]:
            tep.append("H")
        if new[i]==new[i+1]:
            tep.append("E")
    if "E" in tep:
        return False
    else:
        for g in range(len(tep)-1):

            if tep[g]==tep[g+1]:
                return False
        else:
            return True
      
def rotate(m):
    n=len(m)
    new=[]
    for i in range(n):
        temp=[]
        for j in range(n-1,-1,-1):
            temp.append(m[j][i])
        new.append(temp)
    return new
