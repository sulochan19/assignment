# Write a function, is_prime, that takes an integer and returns True if the
# number is prime and False if the number is not prime.

def is_prime(num):
    if num >1:
        for x in range(2,num):
            if num % x ==0:
                return False
                break
        else:
            return True
    else:
        return False
print(is_prime(1))
