import csv
import os

from datetime import datetime

from src.database_manager import (
    DatabaseManager
)


class AttendanceLogger:

    def __init__(
        self,
        csv_path="logs/attendance.csv"
    ):

        self.csv_path = csv_path

        self.logged_people = set()

        self.database = (
            DatabaseManager()
        )

        self._create_file()

    def _create_file(self):

        if not os.path.exists(
            self.csv_path
        ):

            with open(
                self.csv_path,
                "w",
                newline=""
            ) as file:

                writer = csv.writer(
                    file
                )

                writer.writerow(
                    [
                        "Name",
                        "Date",
                        "Time"
                    ]
                )

    def mark_attendance(
        self,
        name
    ):

        if name == "UNKNOWN":
            return

        now = datetime.now()

        date = now.strftime(
            "%Y-%m-%d"
        )

        time = now.strftime(
            "%H:%M:%S"
        )

        if self.database.attendance_exists(
            name,
            date
        ):

            return

        with open(
            self.csv_path,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(
                file
            )

            writer.writerow(
                [
                    name,
                    date,
                    time
                ]
            )

        self.database.add_attendance(
            name,
            date,
            time
        )

        print(
            f"[ATTENDANCE] {name} logged"
        )