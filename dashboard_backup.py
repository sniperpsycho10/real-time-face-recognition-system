import tkinter as tk

from tkinter import (
    ttk,
    messagebox,
    simpledialog
)

import os
import subprocess

from capture_faces import capture_faces
from src.database_manager import DatabaseManager


class FaceRecognitionDashboard:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "Face Recognition Attendance System"
        )

        self.root.geometry(
            "1800x900"
        )

        self.root.minsize(
            1000,
            700
        )

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Face Recognition Attendance System",
            font=(
                "Arial",
                28,
                "bold"
            )
        )

        title.pack(
            pady=25
        )

        self.status_label = tk.Label(
            self.root,
            text="System Ready",
            font=(
                "Arial",
                14
            )
        )

        self.status_label.pack(
            pady=10
        )

        button_width = 30
        button_height = 2

        register_btn = tk.Button(
            self.root,
            text="Register Person",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.register_person
        )

        register_btn.pack(
            pady=10
        )

        capture_btn = tk.Button(
            self.root,
            text="Capture Faces",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.capture_faces
        )

        capture_btn.pack(
            pady=10
        )

        recognition_btn = tk.Button(
            self.root,
            text="Start Recognition",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.start_recognition
        )

        recognition_btn.pack(
            pady=10
        )

        attendance_btn = tk.Button(
            self.root,
            text="View Attendance",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.view_attendance
        )

        attendance_btn.pack(
            pady=10
        )

        analytics_btn = tk.Button(
            self.root,
            text="View Analytics",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.view_analytics
        )

        analytics_btn.pack(
            pady=10
        )

        exit_btn = tk.Button(
            self.root,
            text="Exit",
            width=button_width,
            height=button_height,
            font=("Arial", 14),
            command=self.root.destroy
        )

        exit_btn.pack(
            pady=25
        )

    def register_person(self):

        person_name = simpledialog.askstring(
            "Register Person",
            "Enter Person Name:"
        )

        if not person_name:
            return

        folder_path = os.path.join(
            "data",
            "known_faces",
            person_name.strip()
        )

        if os.path.exists(
            folder_path
        ):

            messagebox.showwarning(
                "Already Exists",
                f"{person_name} already exists."
            )

            return

        os.makedirs(
            folder_path
        )

        messagebox.showinfo(
            "Success",
            f"{person_name} registered successfully."
        )

    def capture_faces(self):

        person_name = simpledialog.askstring(
            "Capture Faces",
            "Enter Person Name:"
        )

        if not person_name:
            return

        try:

            capture_faces(
                person_name.strip()
            )

            messagebox.showinfo(
                "Success",
                "Face capture completed."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def start_recognition(self):

        try:

            subprocess.Popen(
                ["python", "main.py"]
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def view_attendance(self):

        attendance_window = tk.Toplevel(
            self.root
        )

        attendance_window.title(
            "Attendance Records"
        )

        attendance_window.geometry(
            "1200x700"
        )

        style = ttk.Style()

        style.configure(
            "Treeview",
            rowheight=40,
            font=(
                "Arial",
                12
            )
        )

        style.configure(
            "Treeview.Heading",
            font=(
                "Arial",
                13,
                "bold"
            )
        )

        frame = tk.Frame(
            attendance_window
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        tree = ttk.Treeview(
            frame,
            columns=(
                "ID",
                "Name",
                "Date",
                "Time"
            ),
            show="headings",
            height=20
        )

        tree.heading(
            "ID",
            text="ID"
        )

        tree.heading(
            "Name",
            text="Name"
        )

        tree.heading(
            "Date",
            text="Date"
        )

        tree.heading(
            "Time",
            text="Time"
        )

        tree.column(
            "ID",
            width=100,
            anchor="center"
        )

        tree.column(
            "Name",
            width=300,
            anchor="center"
        )

        tree.column(
            "Date",
            width=300,
            anchor="center"
        )

        tree.column(
            "Time",
            width=300,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        database = DatabaseManager()

        records = database.fetch_all_records()

        for record in records:

            tree.insert(
                "",
                tk.END,
                values=record
            )

        database.close()

    def view_analytics(self):

        import pandas as pd

        try:

            df = pd.read_csv(
                "logs/attendance.csv"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

            return

        analytics_window = tk.Toplevel(
            self.root
        )

        analytics_window.title(
            "Attendance Analytics"
        )

        analytics_window.geometry(
            "900x600"
        )

        text_box = tk.Text(
            analytics_window,
            font=(
                "Arial",
                14
            )
        )

        text_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        report = ""

        report += (
            "===== ATTENDANCE ANALYTICS =====\n\n"
        )

        report += (
            f"Total Records : {len(df)}\n\n"
        )

        report += (
            f"Unique People : {df['Name'].nunique()}\n\n"
        )

        report += (
            "Attendance Count:\n\n"
        )

        report += str(
            df["Name"]
            .value_counts()
        )

        report += "\n\n"

        report += (
            "Attendance By Date:\n\n"
        )

        report += str(
            df["Date"]
            .value_counts()
        )

        text_box.insert(
            tk.END,
            report
        )

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = FaceRecognitionDashboard()

    app.run()