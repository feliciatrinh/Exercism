"""
Notes
- recursive
- base case is n = 1 or n <= 0 (error)

Could also do a simple while loop
"""

def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        num_steps = 0
    elif number % 2 == 0:
        num_steps = 1 + steps(number // 2)
    else:
        num_steps = 1 + steps(3 * number + 1)
    return num_steps

def steps_while(n):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    num_steps = 0
    while n != 1:
        num_steps += 1
        n = (n // 2) if n % 2 == 0 else 3 * n + 1
    return num_steps
