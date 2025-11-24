
#code1 

import psutil, os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss} bytes")  

import time

start = time.perf_counter()   

def euler_phi(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    count = 0
    for k in range(1, n + 1):
        a,b = n, k
        while b:
            a, b = b, a % b
        if a == 1:
            count += 1
    return count
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print("Euler's Totient function for", n, "is", euler_phi(n))

end = time.perf_counter() 


print("Execution time:", end - start, "seconds")


#code2

import psutil, os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss} bytes")  

import time

start = time.perf_counter()  
def mobius(n):
    if n == 1:
        return 1

    factors = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if (n // i) % i == 0:
                return 0
            factors += 1
            n = n // i
            while n % i == 0:
                n = n // i
        i += 1

    if n > 1:
        factors += 1

    if factors % 2 == 0:
        return 1
    else:
        return -1

n = int(input("Enter a positive integer: "))
print("Mobius function for", n, "is", mobius(n))

end = time.perf_counter() 


print("Execution time:", end - start, "seconds")


#code3

import psutil, os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss} bytes")  
import time

start = time.perf_counter()  

def divisor_sum(n):
    total = 0
    i = 1
    while i <= n:
        if n % i == 0:  
            total = total + i
        i = i + 1
    return total


n = int(input("Enter a positive integer: "))
print("Sum of divisors of", n, "is", divisor_sum(n))

end = time.perf_counter() 


print("Execution time:", end - start, "seconds")

#code4

import psutil, os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss} bytes")  
import time

start = time.perf_counter()   
def prime_pi(n):
    count = 0
    num = 2   

    while num <= n:
        is_prime = 1   
        divisor = 2
        while divisor * divisor <= num:   
            if num % divisor == 0:
                is_prime = 0
                break
            divisor = divisor + 1
        if is_prime == 1:
            count = count + 1
        num = num + 1

    return count

n = int(input("Enter a positive integer: "))
print("Number of primes up to", n, "is", prime_pi(n))
end = time.perf_counter() 
print("Execution time:", end - start, "seconds")

#code5

import psutil, os

process = psutil.Process(os.getpid())
print(f"Memory usage: {process.memory_info().rss} bytes")  

import time

start = time.perf_counter()  
def legendre_symbol(a, p):
    if a % p == 0:
        return 0

    exp = (p - 1) // 2
    result = 1
    base = a % p

    while exp > 0:
        if exp % 2 == 1:       
            result = (result * base) % p
        base = (base * base) % p
        exp = exp // 2

    if result == 1:
        return 1
    elif result == p - 1:
        return -1
    else:
        return 0   
    print(f"Legendre symbol ({a}/{p}) =", legendre_symbol(a, p))
n = int(input("Enter a positive integer a: "))
p = int(input("Enter a prime number p: "))
print(f"Legendre symbol ({n}/{p}) =", legendre_symbol(n, p))

end = time.perf_counter() 


print("Execution time:", end - start, "seconds")