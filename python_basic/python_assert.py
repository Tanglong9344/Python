
print("Before Assertion.")
assert 1 > 0 # True 则继续执行
print("After Asertion.")

print("Before Assertion.")
try:
    assert 1 < 0  # False 则报错
except Exception as e:
    print('assert is False:',e)
print("After Asertion.")
