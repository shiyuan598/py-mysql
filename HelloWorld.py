from flask import Flask
from flask import request
from flask_cors import *
import pymysql
import json
# import demjson

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/getUsers', methods=['POST', 'GET'])
def index():
    data = request
    print(data)
    name = request.args.get('name')
    return 'Hello World ' + name


@app.route('/getName', methods=['POST'])
def getuser():
    print('jnllle.......')
    db = pymysql.connect('127.0.0.1', 'pyuser', '123456', 'study')
    print('jconnect.......')
    cursor = db.cursor()
    sql = 'select * from study.fish'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print(results)

    return "hhhhhhhh"


@app.route('/getFish', methods=['POST', 'GET'])
def getfish():
    db = pymysql.connect('127.0.0.1', 'root', '123456', 'study')
    cursor = db.cursor()
    sql = 'select * from study.fish'
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    print(results)

    params = request.get_json()
    print(request.method)
    print(params)
    return 'not the post request'


if __name__ == '__main__':
    app.run(debug=True)

# mysql创建用户
# use mysql;
# select * from user;
# CREATE USER 'pyuser'@'127.0.0.1' IDENTIFIED BY '123456';
# GRANT ALL ON *.* TO 'pyuser'@'127.0.0.1';

# mysql报错RuntimeError: cryptography is required for sha256_password or caching_sha2_p
# ALTER USER 'pyuser'@'127.0.0.1'  IDENTIFIED BY 'pwd' PASSWORD EXPIRE NEVER;
# ALTER USER 'pyuser'@'127.0.0.1' IDENTIFIED WITH mysql_native_password BY 'pwd'; #更新一下用户的密码
# FLUSH PRIVILEGES;
# alter user 'pyuser'@'127.0.0.1' identified by '123456';
