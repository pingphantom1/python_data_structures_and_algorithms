prev2 = 0
prev1 = 1

first_18_fibonacci_numbers = [prev2, prev1]

for fibo in range(18):
    newFibo = prev1 + prev2
    first_18_fibonacci_numbers.append(newFibo)
    prev2 = prev1
    prev1 = newFibo

print(f"The first 18 Fibonacci numbers are: {first_18_fibonacci_numbers}")



# Using Recursion to write the fibonacci numbers
print(0)
print(1)
count = 2

def fibonacci(prevFibo1, prevFibo2):
    global count
    if count <= 19:
        newFiboNum = prevFibo1 + prevFibo2
        print(newFiboNum)
        prevFibo2 = prevFibo1
        prevFibo1 = newFiboNum
        count += 1
        fibonacci(prevFibo1, prevFibo2)
    else:
        return


# fibonacci(1, 0)


# Finding the nth fibonacci number using recurssion
def nthFiboNum(n):
    if n <= 1:
        return n
    else:
        return nthFiboNum(n - 1) + nthFiboNum(n - 2)

print(f"The nth Fibonacci number for n provided is: {nthFiboNum(26)}")