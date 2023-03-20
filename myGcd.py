def primeList(number):
    prime = [True for i in range(number+1)]
    p = 2
    while p*p <= number:
        if prime[p]:
            for i in range(p*2, number+1, p):
                prime[i] = False
        p +=1

    primes =[]
    n=2
    while n<len(prime):
        if prime[n]:
            primes.append(n)
        n +=1
    return primes

def findPrimeofNumber(number):
    prime_list= primeList(number)
    p =[]
    for i in range(len(prime_list)):
        while number % prime_list[i] == 0:
            p.append(prime_list[i])
            number = number / prime_list[i]
    return p

def findGcd(number1,number2):
    gcd =1
    prime_list =primeList(min(number1,number2))
    p=[]
    for  i in range(len(prime_list)):
        while number1 % prime_list[i] == 0 and number2 % prime_list[i] ==0:
            p.append(prime_list[i])
            gcd = gcd * prime_list[i]
            number1 = number1 / prime_list[i]
            number2 = number2 / prime_list[i]
    return p,gcd

