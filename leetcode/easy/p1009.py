def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    elif n == 2:
        return '11'
    num = countAndSay(n - 1)
    s, c = '', 1
    for i in range(len(num) - 1):
        # if i == len(num) - 1:
        #     s += str(c) + str(num[i])
        #     break
        if num[i] == num[i + 1]:
            c += 1
        else:
            s += str(c) + num[i]
            c = 1
    s += str(c) + num[-1]
    return s


print(countAndSay(4))
print(countAndSay(5))
print(countAndSay(6))
