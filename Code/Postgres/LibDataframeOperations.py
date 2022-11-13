import psycopg2
from collections import OrderedDict

# variables

hostname = 'localhost'
username = 'postgres'
Pwd = 0
port_id = 5432


conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = Pwd,
            port = port_id)

cur = conn.cursor()



def makeInsertStringFromDictionary(dictionary):
    coloumns = list(dictionary.keys())
    #
    position = "insert into student ("
    for r in range(0,len(coloumns)):
        position = position + coloumns[r] + ","
        if r == len(coloumns) - 1:
            position = position[:-1] + ")"
    #
    element = 'values ('
    for coloumn in coloumns:
        if isinstance(dictionary[coloumn], str):
            element = element + "'" + dictionary[coloumn] + "'" + ','
        elif isinstance(dictionary[coloumn], int):
            element = element + str(dictionary[coloumn]) + ','
    #
    element = (element[:-1]) + ')'
    full_string = position + ' ' + element
    return full_string

def insertPostgresDatabse(database, table_name, data_to_insert):
    import psycopg2
    from collections import OrderedDict
    
    # variables
    
    hostname = 'localhost'
    username = 'postgres'
    Pwd = 0
    port_id = 5432
    
    
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = Pwd,
                port = port_id)
    
    cur = conn.cursor()
    #
    if isinstance(data_to_insert, dict):
        insert = makeInsertStringFromDictionary(data_to_insert)
        cur.execute(insert)
        conn.commit()
    #
    elif isinstance(data_to_insert, list):
        for dictionary in data_to_insert:
            insert = makeInsertStringFromDictionary(dictionary)
            cur.execute(insert)
            conn.commit()


def deletePostgresDatabse(database='', table_name='', data_to_delete)





