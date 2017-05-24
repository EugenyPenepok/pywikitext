import psycopg2
import MySQLdb

import configparser, os

class DataBaseConfig:
    # Установить соединение с базой
    def __init__(self, typeOfDB, host, user, password, database):
        self.conn = 0
        #MySQL
        if typeOfDB == "MYSQL":
            try:
                self.conn = MySQLdb.connect(host=host, user=user,
                                       passwd=password, db=database)
                print('Success connection to MYSQL')
            except MySQLdb.Error as err:
                print("Connection to MYSQL error: {}".format(err))
        # Postgres
        elif typeOfDB == "PGSQL":
            try:
                self.conn = psycopg2.connect(host=host, user=user,
                                       password=password, database=database)
                print('Success connection to PGSQL')
            except MySQLdb.Error as err:
                print("Connection to PGSQL error: {}".format(err))

    # Закрыть соедиение
    def closeDBConnection(self):
        self.conn.close()

    def getDBInfo(self):
        sql = "SELECT * FROM wood_order LIMIT 3"
        try:
            cur = self.conn.cursor()
            # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # by column name
            cur.execute(sql)
            data = cur.fetchall()
            print(data)
        except psycopg2.Error as err:
            print("Query error: {}".format(err))

# test
print(os.getcwd())
config = configparser.ConfigParser()
config.read('config.ini')
dbType = ''
if 'PGSQL' in config and 'MYSQL' in config:
    print('Specify DB:')
    dbtype = input().upper()
elif 'PGSQL' in config:
    dbtype = 'PGSQL'
elif 'MYSQL' in config:
    dbtype = 'MYSQL'

try:
    db = DataBaseConfig(dbtype, config[dbtype]['Host'], config[dbtype]['Username'],
                        config[dbtype]['Password'], config[dbtype]['Database'])
except KeyError as err:
    print("Wrong DB type: {}".format(err))

print(db.getDBInfo())


