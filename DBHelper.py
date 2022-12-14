import pymysql as p
import csv

class DBHelper:
    def __init__(self):
        conn = p.connect(host='localhost', user='root', passwd='mirim', charset='utf8') # mysql 접속
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS famous_vegetables_db")   #db생성
        #mysql 로그아웃 후
        cur.close()
        conn.close()
        #db로 다시접속 (접속한 데이터 베이스 이름 : database='famous_vegetables_db')
        conn = p.connect(host='localhost', user='root', passwd='mirim',database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        #테이블 생성
        cur.execute("CREATE TABLE IF NOT EXISTS saying_tb(saying_num INT PRIMARY KEY AUTO_INCREMENT, saying TEXT, saying_from VARCHAR(50), category VARCHAR(50))")
        cur.execute("CREATE TABLE IF NOT EXISTS user_tb(user_name VARCHAR(50), saying_num INT)")
        cur.execute("CREATE TABLE IF NOT EXISTS diary_tb(diary_num INT PRIMARY KEY AUTO_INCREMENT, diary_date DATE, diary_saying INT, diary_text TEXT)")
        cur.execute("SELECT * FROM saying_tb")
        result = cur.fetchone()
        if result is None:
            f = open('명언.csv', encoding='UTF8')
            csvReader = csv.reader(f)
            for row in csvReader:
                saying = (row[0])
                saying_from = (row[1])
                category = (row[2])
                cur.execute("insert into saying_tb (saying, saying_from, category) values('"+saying+"','"+saying_from+"','"+ category+"')")
            conn.commit()
            f.close()
        cur.close()
        conn.close()
    def get_saying_tb(self):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM saying_tb")
        return cur.fetchall()
    def get_diary_tb(self):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM diary_tb")
        return cur.fetchall()
    def get_diary_view(self, date_diary):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM diary_tb WHERE diary_num = %s", date_diary)
        return cur.fetchall()
    def get_saying_view(self, index_num):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("SELECT * FROM saying_tb WHERE saying_num = %s", index_num)
        return cur.fetchall()
    def insert_saying_tb(self, name_saying, saying,  category):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("insert into saying_tb (saying, saying_from, category) values('" + saying + "','" + name_saying + "','" + category + "')")
        conn.commit()

    def insert_diary_tb(self, get_date, index, get_diary):
        conn = p.connect(host='localhost', user='root', passwd='mirim', database='famous_vegetables_db', charset='utf8')
        cur = conn.cursor()
        cur.execute("insert into diary_tb (diary_date, diary_saying, diary_text) values(%s, %s, %s)",  (get_date, index, get_diary))
        conn.commit()

if __name__ == '__main__':
    db = DBHelper()