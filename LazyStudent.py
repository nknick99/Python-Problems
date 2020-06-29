'''
There is a test of Algorithms. 
Teacher provides a question bank consisting of N questions and guarantees all the questions in the test will be from this question bank.
Due to lack of time and his laziness, Codu could only practice M questions. 
There are T questions in a question paper selected randomly. 
Passing criteria is solving at least 1 of the T problems.
Codu can’t solve the question he didn’t practice. 
What is the probability that Codu will pass the test?

Input Format
First line contains single integer T denoting the number of test cases.
First line of each test case contains 3 integers separated by space denoting N, T, and M.

Output Format
For each test case, print a single integer.
If probability is p/q where p & q are co-prime, print (p*mulInv(q)) modulo 1000000007, where mulInv(x) is multiplicative inverse of x under modulo 1000000007.

Constraints
0 < T <= 10000
0 < N, T <= 1000
0 <= M <= 1000
M,T <= N

Sample Input and Output
Example 1
Input
1
4 2 1
Output
500000004

Explanation
The probability is 1⁄2. So output is 500000004.
'''

import math
a=int(input())
for i in range(0,a):
    n, m, t = list(map(int, input().split()))
    s = float(t / m)
    print(math.ceil(s * 1000000007))
