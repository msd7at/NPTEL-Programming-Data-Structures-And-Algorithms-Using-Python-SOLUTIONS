"""
Week 2 Programming Assignment
Due on 2023-02-09, 23:59 IST
Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 15 private test cases, 5 for each function below, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
A positive integer m can be partitioned as primes if it can be written as p + q where p > 0, q > 0 and both p and q are prime numbers.

Write a Python function primepartition(m) that takes an integer m as input and returns True if m can be partitioned as primes and False otherwise. (If m is not positive, your function should return False.)

Here are some examples of how your function should work.

>>> primepartition(7)
True

>>> primepartition(185)
False

>>> primepartition(3432)
True
Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

Here are some examples to show how your function should work.

 
>>> matched("zb%78")
True

>>> matched("(7)(a")
False

>>> matched("a)*(?")
False

>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
True
A list rotation consists of taking the first element and moving it to the end. For instance, if we rotate the list [1,2,3,4,5], we get [2,3,4,5,1]. If we rotate it again, we get [3,4,5,1,2].

Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations. If k is not positive, your function should return l unchanged. Note that your function should not change l itself, and should return the rotated list.

Here are some examples to show how your function should work.

>>> rotatelist([1,2,3,4,5],1)
[2, 3, 4, 5, 1]

>>> rotatelist([1,2,3,4,5],3)
[4, 5, 1, 2, 3]

>>> rotatelist([1,2,3,4,5],12)
[3, 4, 5, 1, 2]
"""

#ANSWER

import math
def prime(n):
  m=int(math.sqrt(n))
  for i in range(2,m+1):
    if(n%i==0):
      return False
  return True
    
def primepartition(n):
  i=1
  j=n-1
  ans=False
  while(i<j):
    if(prime(i) and prime(j)):
      ans=True
    i=i+1
    j=j-1
  return ans

def matched(s):
  p=0
  for i in s:
    if(i=="("):
      p=p+1
    elif (i==")"):
      p=p-1
    if(p<0):
      return False
    
  if(p==0):
    return True
  return False
def rotatelist(list1,k):
  while(k!=0):
    temp=list1[1:]+list1[0:1]
    list1=temp
    k=k-1
  return list1
###########

import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "primepartition":
   arg = parse(farg)
   print(primepartition(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "rotatelist":
   (arg1,arg2) = parse(farg)
   myarg1 = arg1[:]
   rotatelist(arg1,arg2)
   if myarg1 == arg1:
     print(rotatelist(arg1,arg2))
   else:
     print("Illegal side effect")
else:
   print("Function", fname, "unknown")
