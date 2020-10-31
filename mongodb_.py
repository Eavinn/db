"""
mongodb三要素：数据库，集合，文档

mongo 连接数据库
db 查看当前数据库
show dbs 查看所有数据库
use db_name 切换数据库
db.dropDatabase() 删除当前数据库

show collections 查看集合
db.集合名称.drop() 删除集合

db.集合名称.insert([{key:value, key:value,}, {}]) 插入
db.集合名称.update(<query> ,<update>,{multi: <boolean>}) 更新
db.集合名称.remove(<query>,{justOne: <boolean>}) 删除

db.集合名称.find({条件文档}) 查询
db.集合名称.aggregate({$group: {_id:'$分组字段名', 显示字段:{$统计函数: '$统计字段'}}},) 管道查询group
$group： 将集合中的⽂档分组， 可⽤于统计结果
$match： 过滤数据， 只输出符合条件的⽂档
$project： 修改输⼊⽂档的结构， 如重命名、 增加、 删除字段、 创建计算结果
$sort： 将输⼊⽂档排序后输出
$limit： 限制聚合管道返回的⽂档数
$skip： 跳过指定数量的⽂档， 并返回余下的⽂档
$unwind： 将数组类型的字段进⾏拆分

db.集合.ensureIndex({属性:1},{unique:true})，1表示升序， -1表示降序。 建立索引
db.集合.getIndexes()
db.集合。dropIndex({索引字段: 1})

mongodump -h ip:port -d db名 -o 目录    备份文件
mongorestore -h ip:port -d db名 --dir 目录    恢复文件

"""

from pymongo import MongoClient


class Mongo(object):
    def __init__(self):
        client = MongoClient('mongodb://meng:ml6666@192.168.49.150:27017')
        print(client)
        self.collection = client['test']['t']

    def insert_one(self):
        self.collection.insert_one({'name': '赵丽颖', 'age': 22})

    def insert_many(self):
        data = [{'name': 'user_{}'.format(i), 'age': i} for i in range(30)]
        self.collection.insert_many(data)

    def update_one(self):
        self.collection.update_one({'name': '赵丽颖'}, {'$set': {'name': '迪丽热巴'}})

    def update_many(self):
        self.collection.update_many({'age': 22}, {'$set': {'name': '周冬雨'}})

    def find_one(self):
        res = self.collection.find_one({'age': 22})
        print(type(res), res)

    def find_many(self):
        cursor = self.collection.find({'age': {'$gt': 22}})
        # 使用js代码查询,自定义条件效率不如python
        cursor = self.collection.find({"$where": "function(){return this.age > 25;}"})
        for res in cursor:
            print(res)

    def delete_one(self):
        self.collection.delete_one({'age': 22})

    def delete_many(self):
        self.collection.delete_many({'age': 22})
        # 使用正则表达式
        self.collection.delete_many({'name': {'$regex': 'user'}})


if __name__ == '__main__':
    mg = Mongo()
    mg.find_many()
