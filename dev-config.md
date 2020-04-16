# Python开发环境配置：
+ [python安装](https://www.python.org/downloads/windows/)
+ [pip安装](https://pypi.org/project/pip/#files)
	+ python setup.py install
+ PyQt5安装：pip install PyQt5 -i https://mirrors.aliyun.com/pypi/simple
+ qtdesigner安装:pip install PyQt5-tools -i https://mirrors.aliyun.com/pypi/simple
+ test.ui->test.py:pyuic5 -o test.py test.ui
+ python项目打包:
	+ 下载解压版 执行命令:python setup.py install
	+ pyinstaller -F -w -i icon.ico main.py --add-data sdk;sdk -n main2
	```
	-F表示打包成单个exe文件，不会把组件放到exe外
	-w表示执行时不显示cmd窗口
	-i icon.ico 表示使用icon.ico作为图标
	main.py表示将要打包的py脚本对象
	--add-data sdk;sdk表示额外资源(src(原来的名称);dest(打包后的名称))
	-n main2表示要打包的名称
	```
	---
	pyinstaller -i icon.ico main.py --add-data sdk;sdk -n 体温监测
	pyinstaller -w -i icon.ico main.py --add-data sdk;sdk -n HumanTemperatureMonitor
+ 配置文件解析：pip3 install configparser
+ cv2安装:pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
+ chart安装:pip install PyQtChart -i https://mirrors.aliyun.com/pypi/simple
+ PIL 图形库:pip install pillow
+ pyserial安装:pip install pyserial
+ pyecharts安装 pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts(pip install pyecharts -U)

# 参考资料
+ [PyQt Chart Documentation](http://python.6.x6.nabble.com/PyQt-Chart-Documentation-td5198102.html#none)
+ [折线图-自定义坐标轴](https://blog.csdn.net/chang0522/article/details/90485455)
+ [折线图](https://blog.csdn.net/u011218356/article/details/88957823)
+ [PyQt5 tutorial](http://zetcode.com/gui/pyqt5/)