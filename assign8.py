#code1

import random
import time

def is_prime_miller_rabin(n, k=20):
   
    
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    

   
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    

 
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        
        if x == 1 or x == n - 1:
            continue

       
        for _ in range(s - 1):
            x = (x * x) % n
            if x == 1:
                return False
            
            if x == n - 1:
                break
        else:
            return False
        
            
    return True


st=time.perf_counter()
number1 = 17
result1 = is_prime_miller_rabin(number1)
print(result1)

number2 = 561 
result2 = is_prime_miller_rabin(number2, k=10)
print(result2)
et=time.perf_counter()
duration=et-st
print(f"duration:{duration:.6f}")


#code2

import time
import random 
import math



def modular_pow(base, exponent,modulus):


  
    result = 1

    while (exponent > 0):

    
        if (exponent & 1):
            result = (result * base) % modulus


       
        exponent = exponent >> 1


    
        base = (base * base) % modulus
    
    return result



def pollard_rho(n):


   
    if (n == 1):
        return n


    if (n % 2 == 0):
        return 2



    x = (random.randint(0, 2) % (n - 2))
    y = x


 
    c = (random.randint(0, 1) % (n - 1))


  
    d = 1


 
    while (d == 1):

    
        x = (modular_pow(x, 2, n) + c + n)%n


        y = (modular_pow(y, 2, n) + c + n)%n
        y = (modular_pow(y, 2, n) + c + n)%n


        d = math.gcd(abs(x - y), n)


   
        if (d == n):
            return pollard_rho(n)
    
    return d

st=time.perf_counter()
print("the prime factors of 12 are:",pollard_rho(12))
print("the prime factors of 4 are:",pollard_rho(4))
print("the prime factors of 187 are:",pollard_rho(187))
et=time.perf_counter()
duration=et-st
print(f"duration:{duration:.6f}")



#code3


import time
def zeta_approx(s, terms):
    
    if terms <= 0:
        return 0.0

    zetasum = 0.0
    for n in range(1, terms + 1):
        zetasum += 1.0 / (n ** s)
    return zetasum
st=time.perf_counter()
s_value = 3
num_terms = 1000
approx_zeta = zeta_approx(s_value, num_terms)
print(approx_zeta)
et=time.perf_counter()
duration=et-st
print(f"duration:{duration:.6f}")


#code4

import time

def partitions(n):

    p = [0] * (n + 1)


   
    p[0] = 1

    for i in range(1, n + 1):
        k = 1
        while ((k * (3 * k - 1)) / 2 <= i) :
            p[i] += ((1 if k % 2 else -1) * 
                    p[i - (k * (3 * k - 1)) // 2])

            if (k > 0):
                k *= -1
            else:
                k = 1 - k

    return p[n]

st=time.perf_counter()
print(partitions(7))
print(partitions(20))
print(partitions(11))
et=time.perf_counter()
duration=et-st
print(f"duration:{duration:.6f}")