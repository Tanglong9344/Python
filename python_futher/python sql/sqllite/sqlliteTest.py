import sqlite3

conn = sqlite3.connect('data.db') # 不存在则创建
print("Opened database successfully")

c = conn.cursor()

# 创建表
try:
    c.execute('''CREATE TABLE user
           (ID INT PRIMARY KEY    NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL);''')
    print("Table created successfully")
except Exception as e:
    print(e)
conn.commit()

# 数据插入
# c.execute("INSERT INTO user (id,name,age) \
#       VALUES (1, 'Paul', 32)")
# c.execute("INSERT INTO user (id,name,age) \
#       VALUES (2, 'Allen', 25 )")
#
# c.execute("INSERT INTO user (id,name,age) \
#       VALUES (3, 'Teddy', 23)")

conn.commit()
print("Records created successfully")

# 数据查询
dataList = c.execute("SELECT * from user where age=23 and id=3 order by age").fetchall()
for i in range(0,len(dataList)):
    print(i)
    print(dataList[0])
print("Operation done successfully")

conn.close()