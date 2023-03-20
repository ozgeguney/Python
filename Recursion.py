def FactorialFunction(n):
    output = 1
    if n<=1 :
        output = 1
    else:
        output = n* FactorialFunction(n-1)
    return output

def FibonacciFunction(n):
    output = 0
    if n<=0:
        output = 0
    elif n==1:
        output = 1
    else:
        output = FibonacciFunction(n-1) + FibonacciFunction(n-2)
    return output

def sumNnumbers(n):
    sum =0
    if n<=0:
        sum =0
    else:
        sum = n + sumNnumbers(n-1)
    return sum

