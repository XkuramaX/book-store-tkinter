import sqlite3
def connect():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
	conn.commit()
	conn.close()
def insert(title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO Book Values(NULL,?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	conn.close()
def view():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM Book")
	row=cur.fetchall()
	conn.close()
	return row
def search(title="",author="",year="",isbn=""):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
	row=cur.fetchall()
	conn.close()
	return rows
def delete(id):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM Book WHERE id=?",(id,))
	conn.commit()
	conn.close()
def update(id,title,author,year,isbn):
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE Book set title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
	conn.commit()
	conn.close()
connect()	