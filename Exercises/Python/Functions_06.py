def fibonacci(n, num = [0, 1]):
    if n in num:
        return n
    while len(num) < n:
        num.append(num[-1] + num[-2])
        fibonacci(n, num)
    return num
    
print(fibonacci(5))











