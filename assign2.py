'''1st program'''

import time
import tracemalloc

tracemalloc.start()
ST=time.time()

def factorial(n):
    if n<0:
        print("Factorial is not defined for negative numbers")
    elif n==0:
        return 1
    else:
        value=1
        for i in range(1,n+1):
            value*=i
        return value


x=-2
result=factorial(x)
y=24
result1=factorial(y)
print (f" The factorial of {y} is {result1} ")

ET=time.time()
duration=ET-ST
current, peak = tracemalloc.get_traced_memory()
print(f" The total duration of the program is:{duration} seconds")
print(f" The total memory used is:{peak} bytes")


''' 2nd program '''
import time
import tracemalloc

tracemalloc.start()
ST=time.time()


def is_palindrome(num):

    if num<0:
        return False
    elif num==0:
        return True

    original=num
    reverse=0

    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num //=10
        if original==reverse:
            return True
         

    

print(f"121 is a palindrome: {is_palindrome(121)}")
print(f"123 is a palindrome: {is_palindrome(123)}")
print(f"-121 is a palindrome: {is_palindrome(-121)}")
print(f"0 is a palindrome: {is_palindrome(0)}")

ET=time.time()
duration=ET-ST
current, peak = tracemalloc.get_traced_memory()
print(f" The total duration of the program is:{duration} seconds")
print(f" The total memory used is:{peak} bytes")


'''3rd program'''
import time
import tracemalloc

tracemalloc.start()
ST=time.time()

def mean_of_digits(n):
    digiSum, digiLen = 0, 0

    while n:
        digiLen += 1
        digiSum += n % 10
        n = n//10
    return(digiSum/digiLen)

print (" The average of digits is:",mean_of_digits(567))
print (" The average of digits is:",mean_of_digits(76547))

ET=time.time()
duration=ET-ST
current, peak = tracemalloc.get_traced_memory()
print(f" The total duration of the program is:{duration} seconds")
print(f" The total memory used is:{peak} bytes")


''' 4th program'''

import time
import tracemalloc

tracemalloc.start()
ST=time.time()

def digital_root(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    while n >= 10:
        add = 0
        while n > 0:
            add += n % 10  
            n //= 10              
        n = add
    return n

print("The digital root is:",digital_root(1234))
print("The digital root is:",digital_root(3436))

ET=time.time()
duration=ET-ST
current, peak = tracemalloc.get_traced_memory()
print(f" The total duration of the program is:{duration} seconds")
print(f" The total memory used is:{peak} bytes")


''' 5th program '''
import time
import tracemalloc

tracemalloc.start()
ST=time.time()

def  is_abundant(n):
     if n < 1:
        return False

     add = 0
    
     for i in range(1, n):
        if n % i == 0:
            add += i

     return add > n

print(is_abundant(12))  
print(is_abundant(17))  
print(is_abundant(13))

ET=time.time()
duration=ET-ST
current, peak = tracemalloc.get_traced_memory()
print(f" The total duration of the program is:{duration} seconds")
print(f" The total memory used is:{peak} bytes")