def fibonacci(n):
    # --- 1. THE BASE CASES ---
    # These are the stopping points. Without them, the function 
    # would call itself forever and crash (Stack Overflow).
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # --- 2. THE RECURSIVE STEP ---
    # The function calls itself with smaller numbers (n-1 and n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
number_of_terms = 10

print(f"Fibonacci sequence for first {number_of_terms} terms:")
for i in range(number_of_terms):
    print(fibonacci(i))