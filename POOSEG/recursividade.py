#recursividade

# def fatorial(num):
#     if num == 1:
#         return 1
#     return num*fatorial(num-1)

# print(fatorial(5))

def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(10))