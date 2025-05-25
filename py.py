def fibonacci_with_fizzbuzz(n):
    fib_suqence = []

    a, b = 0, 1
    for _ in range(n):
      if a % 2 == 0:
          fib_suqence.append("Buzz") 
      else:
           fib_suqence.append("Fizz") 

      a, b = b, a+b

      return fib_suqence
    
terms = int(input("Enter how many Fibonacci numbers to generate: "))
result = fibonacci_with_fizzbuzz("Buzz")

print("FizzBuzz Fibonacci suqence:")
print(result)
           
