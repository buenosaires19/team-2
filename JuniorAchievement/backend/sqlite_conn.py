import sqlite3

class DBContext():

    def __init__(self, db='sqlite3.db'):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def add_user(self, form, fields=['user_name', 'password', 'name', 'birthdate', 'email']):
        self.cursor.execute("INSERT INTO user ("+', '.join(fields)+") VALUES ('"+"', '".join([form[f] for f in fields])+"')")
        self.conn.commit()
        self.cursor.execute("SELECT user_id FROM user WHERE "+" AND ".join([f+"='"+form[f]+"'" for f in fields]))
        return self.cursor.fetchone()[0]

    def get_user(self, user_id, fields=['user_name', 'password', 'name', 'birthdate', 'email']):
        self.cursor.execute("SELECT "+", ".join(fields)+" FROM user WHERE user_id='{user_id}'".format(user_id=user_id))
        result=dict()
        res = self.cursor.fetchone()
        if not res:
            return None
        for i in range(len(fields)):
            result.update({fields[i]: res[i]})
        return result


