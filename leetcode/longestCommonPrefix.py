def longestCommonPrefix1(strs):
    if not strs: return ""
    minStr = min(strs)
    maxStr = max(strs)
    for i, x in enumerate(minStr):
        if x != maxStr[i]:
            return maxStr[:i]
    return minStr

def longestCommonPrefix2(strs):
    if not strs: return ""
    # strs.sort(key = lambda i:len(i))
    strs.sort()
    minStr = strs[0]
    maxStr = strs[len(strs)-1]
    for i, x in enumerate(minStr):
        if x != maxStr[i]:
            return maxStr[:i]
    return minStr

def longestCommonPrefix3(strs):
    if not strs: return ""
    str = strs[0]
    print(str)
    for s in strs:
        while s.startswith(str) == False:
            if len(str) <= 1:
                return ""
            str = str[:len(str)-1]
    return str

def longestCommonPrefix(strs):
    if not strs: return ""
    ss = list(map(set, zip(*strs)))
    res = ""
    for i, x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

if __name__ == '__main__':
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = ["aa","a"]
    result = longestCommonPrefix3(strs3)
    print('result:',result)