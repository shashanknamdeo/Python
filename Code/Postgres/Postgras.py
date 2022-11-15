psql -U postgres

import psycopg2

hostname = 'localhost'
database = 'shashank'
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

create = """ CREATE TABLE instrument_statistics(
                instrument_name      TEXT NOT NULL,
                trading_date         TEXT NOT NULL,
                backtesting_date     TEXT NOT NULL,
                high_low_range       INTEGER,
                trading_day_type     TEXT,
                gapup_gapdown_flag   TEXT,
                gapup_gapdown_points INTEGER,
                comments             TEXT)"""

create = """create table student (
                id    int,
                name    varchar(20),
                class    int,
                mobile    int) """

cur.execute(create)

insert = "insert into student (id,name,class,mobile) values (1,'shree',11,0755)"

cur.execute(insert)

conn.commit()