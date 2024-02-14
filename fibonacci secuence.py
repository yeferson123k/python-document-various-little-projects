def generate_fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

num_terms = int(input("Enter the number of terms for the fibonacci sequence: "))

fibonacci_sequence = generate_fibonacci(num_terms)
print("fibonacci Sequence: ")
print(fibonacci_sequence)
