import pymysql
def initializeDB():
    db = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='root',
                    db='CarTintServices',
                    charset='utf8mb4',
                    port=3306,
                    cursorclass=pymysql.cursors.DictCursor,
                    autocommit=True
                )
    cursor = db.cursor()
    return [db, cursor]


def writeToDB(dataList,tableName):
        print("Writing to db")
        db, cursor = initializeDB()
        try:
            column_name = list(dataList.keys())
            column_values = list(dataList.values())
            column_values=str(column_values).replace('[',"").replace("]","")
            #map_mod_sign = re.sub(r',\s*$', '', '%s, '*len(column_name))
            TABLE_NAME=tableName
            column_name = '`,`'.join(column_name)
            sql = 'INSERT INTO `%s` (`%s`) VALUES (%s)' %(TABLE_NAME, column_name, column_values)
           # print(sql)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            print(e)