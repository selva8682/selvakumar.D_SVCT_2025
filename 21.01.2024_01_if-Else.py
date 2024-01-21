#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of 6 to 20 , print Weird
#If  is even and greater than 20, print Not Weird
#Input Format

#A single line containing a positive integer, .

#Constraints
#1<=n<=100
#Print Weird if the number is weird. Otherwise, print Not Weird.

#3
#Sample Output 0

#Weird
#Explanation 0
#n=3
# 3 is odd and odd numbers are weird, so print Weird.

#Sample Input 1

#24
##Not 

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 !=0:
        print("Weird")
    elif n%2==0 and 2<n<5:
        print("Not Weird")
    elif n%2==0 and 6<n<20:
        print("Weird")
    elif n%2==0 and n>=20:
        print("Not Weird")
    