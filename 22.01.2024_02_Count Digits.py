#Given an integer N, write a program to count the number of digits in N.

#Input Format

#Example 2: Input1: N = 8394

#Constraints

#n <= 10000

#Output Format

#Output0: 5 Explanation: N has 5 digits

#Output1: 4 Explanation: N has 4 digits

#Sample Input 0

#12345
#Sample Output 0

#5
#Sample Input 1

#876349
#Sample Output 1

#6

n=int(input())
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)