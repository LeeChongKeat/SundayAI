import sqlite3

class Database:
    
    def __init__(self):
        self.connection = sqlite3.connect("/home/pi/Sunday.db")
        self.cursor = self.connection.cursor()
        
    
    def get_users_action(self):
        results = self.cursor.execute("Select * from user_action").fetchall()
        return results
    
    def insert_new_event(self, action_name, pressure, humidity,temperature):
        try:
            self.cursor.execute("update user_action set action_end = DateTime('now') where action_end is null")
            self.connection.commit()
            self.cursor.execute("INSERT INTO user_action (action_name, pressure, humidity, temperature) values ('"+action_name+"',"+str(pressure)+","+str(humidity)+","+str(temperature)+")")
            self.connection.commit()
            return True
        except:
            return False
        
