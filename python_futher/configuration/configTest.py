from configparser import ConfigParser

config = ConfigParser()
config.read('config.conf')
name = config.get("param", "name")
age = config.getint("param", "age")

print('name:%s,age:%d'%(name,18+age))