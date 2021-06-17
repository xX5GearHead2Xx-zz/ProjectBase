import sqlite3
import sys


class SqliteProvider:
    def __init__(self, connection):
        self.connection = connection

    def ExecuteScalar(self, query):
        try:
            conn = sqlite3.connect(self.connection)
            curs = conn.cursor()
            curs.execute(query)
            result = curs.fetchone()[0]
            conn.commit()
            conn.close()
            return result[0]
        except:
            print(sys.exc_info())
            return None

    def ExecuteNonQuery(self, query):
        try:
            conn = sqlite3.connect(self.connection)
            curs = conn.cursor()
            curs.execute(query)
            conn.commit()
            conn.close()
            return True
        except:
            print(sys.exc_info())
            return False

    def ExecuteQuery(self, query):
        try:
            conn = sqlite3.connect(self.connection)
            curs = conn.cursor()
            curs.execute(query)
            result = curs.fetchall()
            conn.commit()
            conn.close()
            return result
        except:
            print(sys.exc_info())
            return None


