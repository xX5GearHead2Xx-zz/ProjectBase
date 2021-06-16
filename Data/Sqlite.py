import sqlite3


class SqliteProvider:
    def __init__(self, connection):
        self.connection = connection

    def ExecuteScalar(self, query):
        conn = sqlite3.connect(self.connection)
        curs = conn.cursor()
        curs.execute(query)
        result = curs.fetchone()[0]
        conn.commit()
        conn.close()
        return result[0]

    def ExecuteNonQuery(self, query):
        conn = sqlite3.connect(self.connection)
        curs = conn.cursor()
        curs.execute(query)
        conn.commit()
        conn.close()
        return True

    def ExecuteQuery(self, query):
        conn = sqlite3.connect(self.connection)
        curs = conn.cursor()
        curs.execute(query)
        result = curs.fetchall()
        conn.commit()
        conn.close()
        return result


