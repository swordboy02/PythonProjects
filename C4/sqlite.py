import sqlite3
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT , count INTEGER)')
fname = input('Enter File Name: ')
fhandle = open(fname)
for line in fhandle:
    if 'From: ' in line:
        line = line.rstrip()
        f = line.split()
        pos = f[1].find('@')
        pos = int(pos)
        org = ((f[1])[pos+1:])
        cur.execute('SELECT count FROM Counts WHERE org = ?' , (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts(org,count) VALUES (?,1)' , (org,))
        else :
            cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?' , (org,))
        conn.commit()
sql = 'SELECT count,org FROM Counts ORDER BY count'
for i in cur.execute(sql) :
    print(str(i[0]),i[1])
cur.close()
conn.close()
