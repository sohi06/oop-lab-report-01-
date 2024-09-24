def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Specify the number of Fibonacci terms you want
num_terms = 10
fib_sequence = fibonacci(num_terms)
print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
