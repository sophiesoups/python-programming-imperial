import math

def is_prime_number(num):
    prime = True
    for divisor in range(2, math.floor(num / 2)):
        if num % divisor == 0:
            prime = False
            break
    return "prime" if prime else "not prime"

print(is_prime_number(29))
        
