def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    leng = len(T)
    result = [0] * leng
    for i in reversed(range(leng-1)):
        j = i+1
        while j < leng:
            if T[i] < T[j]:
                result[i] = j-i
                break
            elif result[j] == 0:
                result[i] = 0
                break
            j += result[j]
    return result

def dailyTemperatures2(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    stack = []
    leng = len(T)
    res = [0] * leng
    for key, value in enumerate(T):
        while stack and T[stack[-1]] < value:
            res[stack[-1]] = key - stack[-1]
            stack.pop()
        stack.append(key)
    return res


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures2(temperatures))