"""
Week 2 Programming Assignment
Due on 2019-08-22, 23:59 IST
Write three Python functions as specified below. Paste the text for all three functions together into the submission window. Your function will be called automatically with various inputs and should return values as specified. Do not write commands to read any input or print any output.
You may define additional auxiliary functions as needed.
In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
For each function, there are normally some public test cases and some (hidden) private test cases.
"Compile and run" will evaluate your submission against the public test cases.
"Submit" will evaluate your submission against the hidden private test cases. There are 10 private test cases, with equal weightage. You will get feedback about which private test cases pass or fail, though you cannot see the actual test cases.
Ignore warnings about "Presentation errors".
Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.

Here are some examples of how your function should work.

  >>> intreverse(783)
  387
  >>> intreverse(242789)
  987242
  >>> intreverse(3)
  3
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
Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.

Here are some examples to show how your function should work.

  >>> sumprimes([3,3,1,13])
  19
  >>> sumprimes([2,4,6,9,11])
  13
  >>> sumprimes([-3,1,6])
  0
"""

#ANSWER

def intreverse(n):
    revno=0
    while n!=0:
        r=n%10
        revno=revno*10 + r
        n=n//10
    return revno

def matched(n):
    n=list(n)
    c=0
    for i in range(len(n)):
        if c==-1:
            return False
        if n[i]=="(":
            c=c+1
        if n[i]==")":
            c=c-1
    if c==0:
        return True
    else:
        return False

def sumprimes(l):
    s=0
    for i in l:
        if i <1:
            s=s+0
        else:
            for j in range(2,i):
                if i % j==0:
                    break
            else:
                s=s+i
    return s   
