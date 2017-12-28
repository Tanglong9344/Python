# Python Exception
|编号|异常名称|描述|
|:---:|:---:|:---:|
|1|Exception|所有异常的基类|
|2|StopIteration|当迭代器的next()方法没有指向任何对象时引发。|
|3|SystemExit|由sys.exit()函数引发。|
|4|StandardError|除StopIteration和SystemExit之外的所有内置异常的基类。|
|5|ArithmeticError|数据计算出现的所有错误的基类。|
|6|OverflowError|当计算超过数字类型的最大限制时引发。|
|7|FloatingPointError|当浮点计算失败时触发。|
|8|ZeroDivisonError|对于所有的数字类型，当对零进行除数或模数时产生。|
|9|AssertionError|在Assert语句失败的情况下引发。|
|10|AttributeError|在属性引用或分配失败的情况下引发。|
|11|EOFError|当没有来自raw_input()或input()函数的输入并且达到文件结尾时引发。|
|12|ImportError|导入语句失败时引发。|
|13|KeyboardInterrupt|当用户中断程序执行时，通常按Ctrl + c。|
|14|LookupError|所有查找错误的基类。|
|15|IndexError|当序列中没有找到索引时引发。|
|16|KeyError|当在字典中找不到指定的键时引发。|
|17|NameError|当在本地或全局命名空间中找不到标识符时引发。|
|18|UnboundLocalError|当尝试访问函数或方法中的局部变量但未分配值时引发。|
|19|EnvironmentError|在Python环境之外发生的所有异常的基类。|
|20|IOError|在尝试打开不存在的文件时，输入/输出操作失败时触发，例如print语句或open()函数。|
|21|OSError|引起操作系统相关的错误。|
|22|SyntaxError|当Python语法有错误时引发。|
|23|IndentationError|当缩进未正确指定时触发。|
|24|SystemError|当解释器发现内部问题时引发，但遇到此错误时，Python解释器不会退出。|
|25|SystemExit|当Python解释器通过使用sys.exit()函数退出时引发。 如果没有在代码中处理，导致解释器退出。|
|26|TypeError|在尝试对指定数据类型无效的操作或函数时引发。|
|27|ValueError|当数据类型的内置函数具有有效参数类型时引发，但参数具有指定的无效值。|
|28|RuntimeError|产生的错误不属于任何类别时引发。|
|29|NotImplementedError|当需要在继承类中实现的抽象方法实际上没有实现时引发。|
