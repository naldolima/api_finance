import sqlite3
from backend.core.config import Settings

def add_user(conn, user):
    sql = ''' INSERT INTO user(email,password,is_admin,is_active)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid



def main():
    try:
        with sqlite3.connect(Settings.DB_NAME) as conn:
            user = ('user@teste.com', '$2b$12$nhKyKQuC2jOiqwf4vKqaQuyUKtx3avyrpaM2N.QILTgUNTz3kWHJO',True, True)
            user_id = add_user(conn, user)
            print('Created user admin success')


    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()