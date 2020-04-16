# PyMySQL

# 安装 pip
# 1.在easy_install.exe的根目录下打开cmd
# 2.输入easy_install.exe pip
# 3.将pip.exe的路径也添加到环境变量PATH中
# 4.在cmd下输入pip进行测试

# 安装PyMySQL模块-PyMySQL-0.8.0

# 中文乱码问题：
# 打开connections.py文件
# 将DEFAULT_CHARSET的默认值'latin1',改成utf8

import pymysql
# Open connection to database test
db = pymysql.connect("localhost","root","password","test")
# Prepare a cursor object using cursor() method
cursor = db.cursor()
# Execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.execute("SELECT * from user")
# print results
data = cursor.fetchone()
while(data):
    print("Result:",data)
    data = cursor.fetchone()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO 
        mysql_test(id,name, birth_date,study_date)
        VALUES (66, 'Insert_test-2','2017-12-31','2017-12-31')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
   print("Insert successful...")
except:
   # Rollback in case there is any error
   print("Something wrong...")
   db.rollback()

try:
    cursor.execute("SELECT * from user")
    # print results
    data = cursor.fetchall()
    for row in data:
        name = row[1]
        birth_date = row[2]
        study_date = row[3]
        print("name:",name,",birth_date:",birth_date,",stydy_date: ",study_date)
except:
   import traceback
   traceback.print_exc()
   print ("Error: unable to fetch data")

# disconnect from server
db.close()