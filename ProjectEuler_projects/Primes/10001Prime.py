import math
import sys

# sys.setrecursionlimit(10000000)

def is_prime(m_input, prime_array): #checks if the input is prime
    sqrt_input = int(math.sqrt(m_input)) #sqrts input

    if prime_array[-1] >= sqrt_input: #checks inputs against existing prime array if array is sufficiently big
        for x in prime_array:
            if x <= sqrt_input:
                if m_input % x == 0:
                    return False
            else:
                return True # returns true if input does not divide by any primes smaller than sqrt

    else: # if current prime array is not sufficient, manually checks bigger numbers and adds them to prime array
        for x in prime_array:
            if m_input % x == 0:
                return False

        current = prime_array[-1] # sets current value to final value of prime array

        while current <= sqrt_input:
            current += 1
            print("Checking the value of " + str(current) + ".")

            if is_prime(current, prime_array): # if value is prime, adds to prime array
                if is_prime(current, prime_array):
                    print(str(current) + " is prime. It has been added to the array.")

                prime_array.append(current)
                with open("prime_array.txt", "a") as f:
                    f.writelines(", " + str(current))
                if m_input % current == 0: # checks input against the new prime
                    return False

        return True

def print_primes(target_prime, prime_array):

    print("\n")
    print("Your target is " + str(target_prime) + ".")
    print("Initial prime array is: " + str(prime_array))
    print("\n")

    if is_prime(target_prime, prime_array):
        print("\n")
        print("Your target, " + str(target_prime) + " is prime!")
    else:
        print("\n")
        print("Your target, " + str(target_prime) + " is not prime.")

    print("Final prime array is: " + str(prime_array))
    print("\n")

def return_prime_index(prime_index):
    prime_array = [2, 3, 5]

    if prime_index == 1:
        value = "st"
    elif prime_index == 2:
        value = "nd"
    elif prime_index == 3:
        value = "rd"
    else:
        value = "th"

    current = prime_array[-1] + 1

    def call(current):

        print(current)

        if len(prime_array) < prime_index:
            if is_prime(current, prime_array):
                prime_array.append(current)
            current += 1
            call(current)

    call(current)
    print("The " + str(prime_index) + value + " prime is " + str(prime_array[prime_index-1]) + "!")

def update_array(file, m_array):
    with open(file) as f:
        var = f.readlines()

    var = str(var)
    for character in "[], '": # replaces each of: ',[] and whitespace with nothing
        var = var.replace(character, '')

    local_array = []
    for x in var:
        local_array.append(int(x))

    m_array = local_array.copy()

prime_array = [2, 3, 5]
is_prime(203, prime_array)
