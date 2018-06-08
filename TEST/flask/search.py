from flask import Flask
from flask import render_template
from flask import request
import pymysql
import json
from django.shortcuts import render_to_response
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = ''
DB_NAME = 'msystem'
DB_CHARSET = 'utf8'
app = Flask(__name__)
@app.route('/')
def shouye():
    return render_template("index.html")
@app.route('/s')
def search():
    #获取关键字
    keyword = request.args.get('wd')
    host = DB_HOST
    port = DB_PORT
    user = DB_USER
    pwd = DB_PWD
    name = DB_NAME
    charset = DB_CHARSET
    conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=name,
                           charset=charset)
    cue = conn.cursor()
    try:
        cue.execute("SELECT id FROM `index`where keyword LIKE %s ORDER BY `index`.`tf-idf` DESC",keyword)
        result = cue.fetchall()
    except Exception as e:
        print('select1 error', e)
    #构造sql查询语句
    sqlstr = ""
    for i in range(0, len(result)):
        str = "'" + "".join(result[i]) + "'"
        if(i<len(result)-1):
           str += ","
        sqlstr += str
    sql = "SELECT * FROM `result` where `index` IN (" + sqlstr + ")"

    try:
         cue.execute(sql)
         result_list = cue.fetchall()
    except Exception as e:
        print("select2 error",e)
    conn.close()
    return render_template('search.html', titles=result_list)
if __name__ == '__main__':
    app.run(debug=True, port=8000)