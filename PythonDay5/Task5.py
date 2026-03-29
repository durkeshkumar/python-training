# Task 5: Memory Optimization (Generator)

def square_generator(n):
    for i in range (1,n+1):
        yield i*i
gen = square_generator(5)

for value in gen:
    print(value)