#!/usr/bin/python
#
#Example of Dynamic Programming 
#http://www.hawstein.com/posts/dp-knapsack.html
#
#Problem description:
'''
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Input:
First line of the input contains no of test cases  T,the T test cases follow.
Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
The next two lines contains the 2 string str1 and str2 .


Output:
For each test case print the length of longest  common subsequence of the two strings .


Constraints:
1<=T<=30
1<=size(str1),size(str2)<=100


Example:
Input:
2
6 6
ABCDGH
AEDFHR
3 2
ABC
AC

Output:
3
2

Explanation
LCS for input Sequences "ABCDGH" and "AEDFHR" is "ADH" of length 3
LCS of "ABC" and "AC" is "AC" of length 2
'''
#

import sys
from fileinput import input

def LCS(str1, str2):
    '''
    return the length of longest common subsequence of str1 and str2
    '''
    len1 = len(str1)
    len2 = len(str2)

    if len1 == 0 or len2 == 0:
        return 0

    if len1== 1:
        if str1[0] in str2:
            return 1
        else:
            return 0
    if len2 == 1:
        if str2[0] in str1:
            return 1
        else:
            return 0

    try:
        #print("=======compare LCS(%s, %s) with 1 + LCS(%s, %s)" % (str1[1:len1], str2, str1[1:len1], str2[str2.index(str1[0])+1 : len2]))
        return max(LCS(str1[1:len1],str2), 1+LCS(str1[1:len1],str2[str2.index(str1[0])+1:len2]))
    except:
        #print("=======Just LCS(%s, %s)" % (str1[1:len1], str2))
        return LCS(str1[1:len1], str2)
    
# need to add the input file as an argument, the data is stored in inputLongestCommonSubsequence.txt, 
# so run this program using $ python LongestCommonSubsequence.py inputLongestCommonSubsequence.txt
file = input(sys.argv[1])
testcases = int(file.next().strip())
for t in range(testcases):
    lens = file.next().strip().split("  ")
    len1 = lens[0]
    len2 = lens[1]
    str1 = file.next().strip()
    str2 = file.next().strip()
    lenOfLCS = LCS(str1, str2)
    print("length of longest common subsequence of %s and %s is %d" % (str1, str2, lenOfLCS))

file.close()
