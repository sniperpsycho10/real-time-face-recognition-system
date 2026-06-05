import sqlite3


class DatabaseManager:

    def __init__(
        self,
        db_path="logs/attendance.db"
    ):

        self.db_path = db_path

        self.connection = sqlite3.connect(
            self.db_path
        )

        self.cursor = (
            self.connection.cursor()
        )

        self.create_table()

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS attendance (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT NOT NULL,

                date TEXT NOT NULL,

                time TEXT NOT NULL

            )
            """
        )

        self.connection.commit()

    def add_attendance(
        self,
        name,
        date,
        time
    ):

        self.cursor.execute(
            """
            INSERT INTO attendance
            (
                name,
                date,
                time
            )
            VALUES
            (?, ?, ?)
            """,
            (
                name,
                date,
                time
            )
        )

        self.connection.commit()

    def fetch_all_records(self):

        self.cursor.execute(
            """
            SELECT *
            FROM attendance
            """
        )

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()