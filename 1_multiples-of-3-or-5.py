#The original Problem can be found at https://projecteuler.net/problem=1

def multipleSum(lim):
    n = 1
    multiples = []
    while n < lim:
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
        n += 1

    return sum(multiples)
print(multipleSum(1000))