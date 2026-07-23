def fibonacci_iterative(n):
    """Generates a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    
 
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

print(fibonacci_iterative(10))

