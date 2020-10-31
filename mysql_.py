"""
RDBMS关系型数据库：建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据
数据库设计三范式：
1NF：列的原子性，一列不能拆分为多列
2NF：表必须有主键，非主键列必须完全依赖主键，不能只依赖于主键的一部分
3NF：非主键列必须直接依赖主键，不能传递依赖

sudo apt-get install mysql-server
sudo service mysql restart

select version()
show databases
use 数据库名
select database()
create database 数据库名 charset=utf8
drop database 数据库名

show tables
desc 表名
show create table 表名
drop table 表名
alter table 表名 rename 表名
alter table 表名 add 列名 类型
alter table 表名 change 原名 新名 类型及约束
alter table 表名 modify 列名 类型及约束
alter table 表名 drop 列名
alter table 表名 add foreign key(列名) references 表名(列名)
alter table 表名 drop foreign key(外键名)

select * from 表名
select 列1,列2,... from 表名
select 列1 as ,列2 as ,... from 表名
select distinct 字段 from 表名
select xx, group_concat(xx) from xx group by xx;
select xx, avg(xx) from xx group by xx having xx;
select xx, count(xx) from xx group by xx with rollup;
select * from 表名 limit start,count
select distinct xx from 表名 where xx group by xx having xx order by xx limit start,count
insert into 表名 values(...)
inert into 表名(列1,...) value (值1,...)
insert into 表名 values(...),(...)...;
insert into 表名(列1,...) values(值1,...),(值1,...)...;
update 表名 set 列1=值1,列2=值2... where 条件
delete from 表名 where 条件

create table xx select xx

事务四大特性(ACID):
原子性，一个事务就是一个最小的工作单元
一致性，数据库总是从一个一致性状态转换到另一个一致性状态
隔离性，一个事务所做做的修改在最终提交前对其他事务不可见
持久性，一旦事务提交修改就会永久保存到数据库
begin commit rollback

show index from 表名
create index 索引名称 on 表名(字段名称(长度))
drop index 索引名称 on 表名
set profiling=1 开启时间检测
show profiles 查看执行时间
grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
drop user '用户名'@'主机';
set password for 用户名@localhost = password('新密码');
alter user 用户名@localhost identified by '新密码';
"""


"""

create table students(
id int unsigned primary key not null auto_increment,
name varchar(20) default "",
cate_id int unsigned,
height decimal(5,2),
gender enum('男','女'),
is_show bit not null default 1,
foreign key (cate_id) references goods_cates(id)
)
"""

from pymysql import *
import time


def main():
    conn = connect(host='192.168.49.132',
                   port=3306,
                   database='jing_dong',
                   user='meng',
                   password='ml6666',
                   charset='utf8')
    cs1 = conn.cursor()
    # params = (4000,)
    # count = cs1.execute('select * from goods where price>%s', params)
    # for idx in range(count):
    #     res_list = [ord(i) if type(i) is bytes else i for i in cs1.fetchone()]
    #     print(res_list)
    # ord可解密mysql中的bit值
    # res = cs1.fetchall()
    t1 = time.time()
    for i in range(100000):
        cs1.execute("insert into test_index values('ha-%d')" % i)
    conn.commit()
    print(time.time()-t1)
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
