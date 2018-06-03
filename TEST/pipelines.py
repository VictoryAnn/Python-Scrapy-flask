# -*- coding: utf-8 -*-
from scrapy.conf import settings
import pymysql
import jieba
import jieba.analyse

import scrapy
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TestPipeline(object):
    # 数据存入json中
    # def __init__(self):
    #     self.file = open('data.json','w',encoding='utf-8')
    # def process_item(self,item,spider):
    #     line = json.dumps(dict(item),ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    # def open_spider(self,spider):
    #     pass
    # def close_spider(self,spider):
    #     pass
    # def __init__(self):
    #     self.host = settings['DB_HOST']
    #     self.port = settings['DB_PORT']
    #     self.user = settings['DB_USER']
    #     self.pwd = settings['DB_PWD']
    #     self.name = settings['DB_NAME']
    #     self.charset = settings['DB_CHARSET']
    #
    #     self.connect()
    #
    # def connect(self):
    #     self.conn = pymysql.connect(host=self.host,port=self.port, user=self.user,password=self.pwd,db=self.name,charset=self.charset)
    #     self.cursor = self.conn.cursor()
    #
    # def close_spider(self, spider):
    #     self.conn.close()
    #     self.cursor.close()
    #
    # def process_item(conn, item, spider):
    #     try:
    #         conn.cursor.execute("""insert into TB(title,link) values("%s", "%s");""", (item.get('title'),item.get('link')))
    #         conn.connect.commit()
    #     except Exception as error:
    #         print(error)
    #     return item
    def process_item(self,item,spider):
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PWD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, db=self.name,
                               charset=self.charset)
        cue = conn.cursor()
        try:
            cue.execute("insert into result(title,link) values(%s, %s);", [item['title'], item['link']])
            print("insert success")  # 测试语句
        except Exception as e:
            print('Insert error:', e)
            conn.rollback()
        else:
            conn.commit()
        try:
            cue.execute("SELECT * FROM result ORDER BY `index` DESC LIMIT 1")
            result = cue.fetchall()
            seg_list = jieba.analyse.extract_tags(result[0][1],topK=20,withWeight=True)
            for line in seg_list:
                self.save(result[0][0], line[0], line[1])
        except Exception as e:
            print('insert error',e)
        print(result[0][0])
        cue.close()
        conn.close()
        return item
    def save(self,index_,keyword,tf_idf):
        host = settings['DB_HOST']
        port = settings['DB_PORT']
        user = settings['DB_USER']
        pwd = settings['DB_PWD']
        name = settings['DB_NAME']
        charset = settings['DB_CHARSET']
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=name,
                               charset=charset)
        cue = conn.cursor()
        try:
            cue.execute("insert into `index`(`id`,`keyword`,`tf-idf`)values(%s,%s,%s);",[index_, keyword, tf_idf])
        except Exception as e:
            print("insert error", e)
            conn.rollback()
        else:
            conn.commit()
        cue.close()
        conn.close()
    # def seg(self,item):
    #     host = settings['DB_HOST']
    #     port = settings['DB_PORT']
    #     user = settings['DB_USER']
    #     pwd = settings['DB_PWD']
    #     name = settings['DB_NAME']
    #     charset = settings['DB_CHARSET']
    #     conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=name,
    #                            charset=charset)
    #     cue = conn.cursor()
    #     try:
    #         cue.execute("SELECT * FROM result ORDER BY `index` DESC LIMIT 1")
    #         result = cue.fetchall()
    #         seg_list = jieba.analyse.extract_tags(result[1],topK=20,withWeight=True)
    #         print(result[0])
    #         for line in seg_list:
    #             self.save(result[0], line[0], line[1])
    #     except Exception as e:
    #         print('insert error',e)
    #     conn.close()
    #     return item
