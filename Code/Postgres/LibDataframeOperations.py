import psycopg2


def makeInsertStringFromDictionary(table_name, dictionary):
    coloumns = list(dictionary.keys())
    #
    position = "INSERT INTO " + table_name + "("
    for r in range(0,len(coloumns)):
        position = position + coloumns[r] + ","
        if r == len(coloumns) - 1:
            position = position[:-1] + ") "
    #
    element = 'VALUES ('
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
    #
    # variables
    hostname = 'localhost'
    username = 'postgres'
    Pwd = 0
    port_id = 5432
    #
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = Pwd,
                port = port_id)
    #
    cur = conn.cursor()
    #
    if isinstance(data_to_insert, dict):
        insert = makeInsertStringFromDictionary(table_name, data_to_insert)
        cur.execute(insert)
        conn.commit()
    #
    elif isinstance(data_to_insert, list):
        for dictionary in data_to_insert:
            insert = makeInsertStringFromDictionary(table_name, dictionary)
            cur.execute(insert)
            conn.commit()


def deletePostgresDatabase(database, table_name, data_to_delete):
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






def fetchAllPostgresDatabase(database, table_name):
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
    select_all = 'SELECT * FROM {0}'.format(table_name)
    cur.execute(select_all)
    row_list = cur.fetchall()
    for row in row_list:
        print(row)