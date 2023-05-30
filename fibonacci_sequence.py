#program for fibonacci_series
def fibonacci_sequence(n):
    sequence = [0, 1] 

    if n <= 1:
        return sequence[:n + 1]

    while len(sequence) <= n:
        
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

# ask user input
user_input = int(input("Enter a number: "))

# Call the fibonacci_sequence method
fib_sequence = fibonacci_sequence(user_input)

# Display the Fibonacci series
print("Fibonacci sequence:")
for number in fib_sequence:
    print(number, end=" ")