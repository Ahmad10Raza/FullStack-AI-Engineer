def cache(func):
    
    memory = {}
    
    def wrapper(n):
        
        if n in memory:
            return memory[n]
        
        result = func(n)
        memory[n] = result
        return result
    
    return wrapper

@cache
def fib(n):
    
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)

print(fib(10))



for i in range(11):
    print(fib(i), end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34 55