# DB API

import MySQLdb
cxn = MySQLdb.connect(user='root')

cxn.query('DROP DATABASE test')
cxn.query('CREATE DATABASE test')
cxn.query("GRANT ALL on test.* to ''@'localhost'")
cxn.commit()
cxn.close()

cxn = MySQLdb.connect(db='test')
cur=cxn.cursor()
cur.execute('CREATE  TABLE users(login VARCHAR(8), userid INT)')
cur.execute("INSERT INTO users VALUES ('john',7000)")
cur.execute("INSERT INTO users VALUES ('bob',7001)")
cur.execute("INSERT INTO users VALUES ('james',7002)")
cur.execute("SELECT * FROM users WHERE login LIKE 'j%'")
for data in cur.fetchall():
    print '%s\t%s' % data