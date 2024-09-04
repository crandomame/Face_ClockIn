import psycopg2
from setting import opengauss_config


def database_init():
    sql = ("CREATE TABLE Employee (ID VARCHAR PRIMARY KEY, Name VARCHAR, ImagePath VARCHAR);"
           "CREATE TABLE history "
           "(Time TIMESTAMP PRIMARY KEY, ID VARCHAR, Name VARCHAR,"
           "Similarity FLOAT(2), IsSuccessful BOOLEAN, FOREIGN KEY (ID) REFERENCES Employee(ID));")
    result = execute_sql(sql)
    print("数据库初始化成功！")
    return result


def execute_sql(sql):
    dsn = "dbname={database} user={user} password={password} host={host} port={port} client_encoding={client_encoding}".format(
        **opengauss_config)

    conn = psycopg2.connect(dsn)  # 连接数据库
    cur = conn.cursor()  # 创建光标：

    cur.execute(sql)  # 执行SQL指令

    if sql.lower().startswith("select"):
        result = cur.fetchall()
    else:
        result = None

    conn.commit()  # 提交事务
    cur.close()  # 关闭光标：
    conn.close()  # 关闭数据库连接：

    return result


if __name__ == '__main__':
    result = database_init()
    print(result)
