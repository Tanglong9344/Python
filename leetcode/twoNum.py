def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    data = {}
    for i in range(0,len(nums)):
        if nums[i] in data.keys():
            return [data[nums[i]],i]
        data[target - nums[i]] = i
    return result



if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums,target))
    f1 = 3.35
    f2 = 3.37
    if f2 > f1:
        print("xxx")

    l1 = {1:"1",2:"2",3:"3"}
    print(l1)
    l1.pop(2)
    print(l1)

    a1 = [1,2,3,4]
    print(a1)
    a1.remove(1)
    print(a1)