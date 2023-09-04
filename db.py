import sqlite3


class ActivityDatabase:
    # I create a ActivityDatabase class that initializes an SQLite database
    # and creates an activities table if it doesn't exist
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(""" 
                CREATE TABLE IF NOT EXISTS activities(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    date DATE
                )
            """)

# The add_activity method allows you to insert activities into the database,
    # providing the name, description, and date as parameters
    def add_activities(self, name, description, date):
        with self.conn:
            self.conn.execute("""
                INSERT INTO activities (name, description, date)
                VALUES (?, ?, ?)
            """, (name, description, date))

# The get_activities method retrieves all activities from the database
    def get_activities(self):
        with self.conn:
            cursor = self.conn.execute("SELECT * FROM activities")
            return cursor.fetchall()

    def close_connection(self):
        self.conn.close()


# Finally, in the __main__ block, an example of how to use this class is provided
if __name__ == '__main__':
    db = ActivityDatabase('activity_database.db')

    #  # Adding an example activity
    db.add_activities("Exercise", "Ran for 30 minutes", "2023-09-02")

    # Retrieving and printing all activities
    activities = db.get_activities()
    for activity in activities:
        print(activity)

    db.close_connection()