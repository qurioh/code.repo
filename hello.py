def fibonacci_with_fizzbuzz(n):
    fib_sequence = []  

    a, b = 0, 1
    for _ in range(n):
        if a % 2 == 0:
            label = "Buzz"
        else:
            label = "Fizz"

        fib_sequence.append((a, label))  
        a, b = b, a + b  

    return fib_sequence


terms = int(input("Enter how many Fibonacci numbers to generate: "))
result = fibonacci_with_fizzbuzz(terms)

print("\nFibonacci FizzBuzz Sequence:")
for num, label in result:
    print(f"{num} → {label}")
