
import sqlite3

conn = sqlite3.connect('test.db')
create_sql = 'create table person(id int primary key not null, name text not null);'
conn.execute(create_sql)
insert_sql = 'insert into table values(?, ?)'
conn.execute(insert_sql, (100, 'LY'))
conn.execute(insert_sql, (200, 'July'))
cursors = conn.execute('select id, emp_name from company')
for row in cursors:
    print(row[0], row[1])
conn.close()
