#Task
#The provided code stub reads two integers, a  and b, from STDIN.

##No rounding or formatting is necessary.

#Example
#b=5
#The result of the integer division 3//5=0
#The result of the float division is 3/5=0.6
#Print:

#0
#0.6
#Input Format

#The first line contains the first integer, a .
#The second line contains the second integer ,b.

#Output Format

#Sample Input 0

#4
#Sample Output 0

#1
#1.33333333333

 if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
