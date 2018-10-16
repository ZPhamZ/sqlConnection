import pypyodbc
import datetime



def sqlQuery():
    connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=serverName;'
                              'Database=databasename;'
                              'uid=username;pwd=password')
    cursor = connection.cursor()
    cursor.execute("sql query")
    row = cursor.fetchone()
    while row:        
        eodDate = row[0]
        print(eodDate)
        row = cursor.fetchone()
    eodDate1 = eodDate.strftime("%Y%m%d")
    print(eodDate1)
    return eodDate1
    connection.close()

def main():
    sqlQuery()

main()
    



