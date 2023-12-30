## leaderboard.py
import sqlite3

class Leaderboard:
    def __init__(self):
        self.conn = sqlite3.connect('leaderboard.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS leaderboard 
                   (name TEXT, score INTEGER)'''
        self.cursor.execute(query)
        self.conn.commit()

    def update_leaderboard(self, name, score):
        query = '''INSERT INTO leaderboard (name, score) 
                   VALUES (?, ?)'''
        self.cursor.execute(query, (name, score))
        self.conn.commit()

    def display_leaderboard(self):
        query = '''SELECT * FROM leaderboard 
                   ORDER BY score DESC LIMIT 10'''
        self.cursor.execute(query)
        leaderboard = self.cursor.fetchall()
        return leaderboard

    def __del__(self):
        self.conn.close()
