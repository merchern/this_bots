import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        print("The database is connected successfully")

    def add_client(self, ID):
        with self.connection:
            try:
                self.cursor.execute("INSERT INTO 'client' VALUES (?, ?, ?)", (ID, "0.0", "client"))
            except: pass

    def get_client_data(self, ID):
        return self.cursor.execute("SELECT * FROM 'client' WHERE user_id = ?", (ID,)).fetchmany()[0]

    def update_client_data(self, ID, balance):
        with self.connection:
            self.connection.execute("UPDATE 'client' SET balance = ? WHERE user_id = ?", (balance, ID,))

    def client_exist(self, ID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'client' WHERE user_id = ?", (ID,)).fetchmany(1)
            if not bool(len(result)):
                return False
            return result[0]

    def get_all_client(self):
        return self.cursor.execute("SELECT user_id FROM 'client'").fetchall()

    def get_all_client_without_ban(self):
        return self.cursor.execute("SELECT user_id FROM 'client' WHERE role = 'client'").fetchall()

    def get_all_client_with_ban(self):
        try:
            return [i[0] for i in self.connection.execute("SELECT user_id FROM 'client' WHERE role = 'ban'").fetchall()]
        except: pass

    def ban_client(self, ID):
        with self.connection:
            self.connection.execute("UPDATE 'client' SET role = 'ban' WHERE user_id = ?", (ID,))

    def unban_client(self, ID):
        with self.connection:
            self.connection.execute("UPDATE 'client' SET role = 'client' WHERE user_id = ?", (ID,))

    def user_exists(self, ID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'referral' WHERE user_id = ?", (ID,)).fetchall()
            return bool(len(result))

    def add_referral(self, user_id, referrer_id=None):
        with self.connection:
            if referrer_id is not None:
                self.cursor.execute("INSERT INTO 'referral' ('user_id', 'referrer_id') VALUES (?, ?)", (user_id, referrer_id,))
            else:
                self.cursor.execute("INSERT INTO 'referral' ('user_id') VALUES (?)", (user_id,))

    def count_referrers(self, ID):
        with self.connection:
            return self.cursor.execute("SELECT COUNT('id') as count FROM 'referral' WHERE referrer_id = ?", (ID,)).fetchone()[0]