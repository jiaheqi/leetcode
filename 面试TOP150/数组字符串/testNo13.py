def romanToInt(str):
    # 个人解法
    # numbers = {
    #     'I': 1,
    #     'V': 5,
    #     'X': 10,
    #     'L': 50,
    #     'C': 100,
    #     'D': 500,
    #     'M': 1000
    # }
    # number = []
    # # 先把罗马数字都映射为阿拉伯数字
    # for m in str:
    #     print(m)
    #     number.append(numbers.get(m))
    # print(number)
    # res = []
    # i = 0
    # # 如果遇到左侧元素小于右侧，那么需要判断是不是满足条件的几种特殊情况
    # while i < len(number):
    #     # 当i走到最后一个元素，直接添加，不需要进行下面的比较，因为i后面已经没有元素，不存在i+1
    #     if i == len(number) - 1:
    #         res.append(number[i])
    #         break
    #     j = i + 1
    #     if number[i] < number[j]:
    #         if number[i] == 1 and number[j] == 5:
    #             res.append(4)
    #         elif number[i] == 1 and number[j] == 10:
    #             res.append(9)
    #         elif number[i] == 10 and number[j] == 50:
    #             res.append(40)
    #         elif number[i] == 10 and number[j] == 100:
    #             res.append(90)
    #         elif number[i] == 100 and number[j] == 500:
    #             res.append(400)
    #         elif number[i] == 100 and number[j] == 1000:
    #             res.append(900)
    #         i += 2
    #     else:
    #         res.append(number[i])
    #         i += 1
    # print(res)
    # sumres = 0
    # # 最后把最终的映射结果相加就是结果
    # for k in res:
    #     sumres = sumres + k
    # print(sumres)
    # return sumres
    # 官方解法
    numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    n = len(str)
    # 结果是一个索引和value的映射，类似于dict的k，v,k是索引，v是字符串的每个字符
    for i, ch in enumerate(s):
        print(f'i:{i}   ch:{ch}')
        value = numbers.get(ch)
        # 如果前一个元素值小于后一个元素，那么最终结果需要减去当前value，比如：value=1，后一个值是5，那么最终的结果其实是+5-1=4，所以如果小于后一个元素，当前元素的值需要减去，后一个元素值正常相加
        if i < n - 1 and value < numbers.get(s[i + 1]):
            ans -= value
        else:
            ans += value
    return ans


if __name__ == '__main__':
    s = "MCMXCIV"
    # s = "LVIII"
    print(romanToInt(s))
