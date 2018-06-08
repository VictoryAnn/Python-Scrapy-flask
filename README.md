# Python-Scrapy-Flask
用scrapy和flask框架搭建简易的搜索引擎
##使用方法
* 执行main.py（爬去网站信息，并建立索引，保存到数据库）
* 执行search.py，进行关键字检索
##数据库配置
settings.py
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = ''
DB_NAME = 'msystem'
DB_CHARSET = 'utf8'
