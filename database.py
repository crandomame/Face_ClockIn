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

    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    cur.execute(sql)

    if sql.lower().startswith("select"):
        result = cur.fetchall()
    else:
        result = None

    conn.commit()
    cur.close()
    conn.close()

    return result


if __name__ == '__main__':
    result = database_init()
    print(result)
