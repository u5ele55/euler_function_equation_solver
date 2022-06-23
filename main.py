# Made by Shaganov Vyacheslav
# student of 1384 group, SPbETU "LETI"

from math import *
from itertools import chain, combinations

print("f(x) = N")
N = int(input("Enter N: "))

def isPrime(n: int):
    for i in range(2, round(n**(1/2)) + 1):
        if n % i == 0:
            return False

    return True

def findMaxDegreeSoThatEulerFunctionLessThanN(p: int, N: int):
    l = floor(log(N, p))
    for k in range(l, max(l**2, l+3)):
        if p**k - p**(k-1) > N:
            return k-1
    print(f'He broke everything, blame him! {p}')
    assert True == False

primes = []
maxDegrees = {}

for i in range(2, N*2):
    if isPrime(i):
        k = findMaxDegreeSoThatEulerFunctionLessThanN(i, N)
        if k != 0:
            primes.append(i)
            maxDegrees[i] = k

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def multiplyAllLoweredByOne(arr: list):
    res = 1
    for i in arr:
        res *= i-1
    return res
    

def phi(factorizationMembers: list, degrees: map):
    res = 1
    
    for i in factorizationMembers:
        ip = i**(degrees[i]-1)
        res *= i*ip - ip
    return res

def numberFromFactorization(factorizationMembers: list, degrees: map):
    res = 1
    for i in factorizationMembers:
        res *= i**degrees[i]
    return res

result = []

for comb in powerset(primes):
    # comb is a list of primes that will be used
    if len(comb) == 0 or multiplyAllLoweredByOne(comb) > N: continue
    
    degrees = {}
    
    for p in comb:
        degrees[p] = 1
    # brute forcing all possible combinations of powers
    while degrees[comb[0]] <= maxDegrees[comb[0]]:
        if phi(comb, degrees) == N:
            result.append(numberFromFactorization(comb, degrees))
        
        for pIndex in range(len(comb)-1, -1, -1):
            if degrees[comb[pIndex]] >= maxDegrees[comb[pIndex]] and pIndex != 0:
                degrees[comb[pIndex]] = 1
            else:
                degrees[comb[pIndex]] += 1
                break
        
print( sorted(result) if len(result) else "No solution!" )
