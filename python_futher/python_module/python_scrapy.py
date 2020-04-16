# python package 'scrapy'
# 1. 新建项目，scrapy startproject projectName
# 新建'projectName'文件夹
# 文件夹下文件：
# scrapy.cfg：项目的配置文件
# projectName/：项目的Python模块，将会从这里引用代码
# projectName/items.py：项目的items文件
# projectName/middlewares.py：项目的中间件文件
# projectName/pipelines.py：项目的pipelines文件
# projectName/settings.py：项目的设置文件
# projectName/spiders/：存储爬虫的目录

# 2. 明确目标(Items), 修改'items.py'文件
# 3. 制作爬虫(Spider)
# name：爬虫标识名称
# start_urls：待爬取的URL列表
# parse：解析方法
# 4. 存储内容(pip line)
import scrapy
import scrapy as sy  # alias

print(sy.item)

# use the built-in dir function to list the identifiers that a module defines.
print(dir(scrapy))
