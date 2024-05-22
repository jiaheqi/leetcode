def hIndex(citations):
    res = {}
    for i in citations:
        tmp = 0
        for j in citations:
            if j >= i:
                tmp += 1
        res[i] = tmp
    print(res)
    result = []
    for k, v in res.items():
        if k <= v:
            result.append(k)
    if not result:
        return 0
    else:
        result.sort()
    print(result[-1])
    return result[-1]


if __name__ == '__main__':
    # citations = [3, 0, 6, 1, 5]
    # citations = [1, 3, 1]
    citations = [100]
    hIndex(citations)
    n = 5
    counter = [0] * (n + 1)
    print(counter)
