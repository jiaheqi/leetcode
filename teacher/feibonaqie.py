def feibonaqie(n):
    """
    求出斐波那契数列第多少项大于2022
    :return:
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return feibonaqie(n - 1) + feibonaqie(n - 2)


x = 1
i = 1
while x <= 2022:
    i = i + 1
    x = feibonaqie(i)
print(i)
