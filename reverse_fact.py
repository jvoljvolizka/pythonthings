def reverse_fact(num):
    num = int(num)
    count = 2
    while num != 1:
        num = num / count
        if num == 0:
            return "NONE"
        count += 1
    return str(count - 1) + "!"
print(reverse_fact(120))
print(reverse_fact(150))
print(reverse_fact(3628800))
print(reverse_fact(479001600))
print(reverse_fact(6))
print(reverse_fact(18))