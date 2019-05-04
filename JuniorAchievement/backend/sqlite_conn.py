import sqlite3

class DBContext():

    def __init__(self, db='backend/sqlite3.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def add_user(self, form, fields=['user_name', 'password', 'name', 'birthdate', 'email']):
        self.cursor.execute("INSERT INTO user ("+', '.join(fields)+") VALUES ('"+"', '".join([form[f] for f in fields])+"')")
        self.conn.commit()
        self.cursor.execute("SELECT user_id, "+", ".join(fields)+" FROM user WHERE "+" AND ".join([f+"='"+form[f]+"'" for f in fields]))
        result={'user_id': self.cursor.fetchone()[0]}
        for i in range(len(fields)):
            result.update({fields[i]: form[fields[i]]})
        return result


    def get_user(self, user_name, password, fields=['user_id', 'user_name', 'password', 'name', 'birthdate', 'email']):
        self.cursor.execute("SELECT "+", ".join(fields)+" FROM user WHERE user_name='{user_name}' AND password='{password}'".format(user_name=user_name, password=password))
        result=dict()
        res = self.cursor.fetchone()
        if not res:
            return None
        for i in range(len(fields)):
            result.update({fields[i]: res[i]})
        return result

