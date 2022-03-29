"""
Description:
We want to generate a function that computes the series starting from 0 and ending until the given number.
Example:
Input:> 6
Output:0+1+2+3+4+5+6 = 21
Input:> -15
Output:-15<0
Input:> 0
Output:0=0"""


def show_sequence(n):
    sum = 0
    strin =""
    liste = []
    a =""
    if n > 0 :
        for i in range(n+1):
            sum += i
            liste.append(i)
        for i in liste:
            strin += str(i) 
            pass
            strin += "+"
        return strin + " = " + f"{sum}"
    elif n ==0:
        return "0=0"
    elif n < 0 :
        return f"{n}<0"

show_sequence(5)
