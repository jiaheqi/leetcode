def strStr( haystack: str, needle: str):
    # split_len = len(needle)
    # for i in range(len(haystack)-split_len+1):
    #     print(haystack[i:i+split_len])
    #     if haystack[i:i+split_len] == needle:
    #         return i
    # return -1
    return haystack.find(needle)
    # return haystack.index(needle) if needle in haystack else -1


if __name__ == '__main__':
    # haystack = "sadbutsad"
    # needle = "sad"
    # haystack = "leetcode"
    # needle = "leeto"
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack,needle))
