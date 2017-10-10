# random 随机数
#示例1,整数
print ("示例1,整数：")
import random
num = random.randint(1,10)
print (num)

#示例2,浮点数
print ("示例2,浮点数：")
import random
num = random.random() #生成一个0到1之间的随机浮点数
print (num)

#示例3,浮点数
print ("示例3,浮点数：")
import random
num = random.uniform(1,10)
print (num)

#示例4
print ("示例4：")
import random
list = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]
num = random.choice(list) #从list随机选取一个元素
print (num)

#示例5
print ("示例5：")
import random
num = random.randrange(1,20,3) #从1 到 10，间隔为 3的随机数
print (num)                    #即从[1，4,7,10,13,16,19]中选择

#示例6
#从1 到 10，间隔为 3的随机数
#即从[1，4,7,10,13,16,19]中选择
#和示例5等价
print ("示例6：")
import random
num = random.choice(range(1,20,3))
print (num)

#示例7
print ("示例7：")
import random
list = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]
num = random.sample(list, 3) #从list随机选取3个元素组成一个新序列
print (num)