def fib_OK(n):
    tab = [0, 1]
    if n == 0:
        return 0
    for _ in range(2, n + 1):
        tab.append(tab[-1] + tab[-2])
    return tab[-1]

def fib_Error(n):
    return fib_OK(n + 2)