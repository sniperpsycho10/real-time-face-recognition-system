import customtkinter as ctk

from tkinter import messagebox

import subprocess

import os

import sys


PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

if PROJECT_ROOT not in sys.path:

    sys.path.append(
        PROJECT_ROOT
    )


class AttendancePage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#111827"
        )

        title = ctk.CTkLabel(
            self,
            text="Attendance",
            font=ctk.CTkFont(
                size=40,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="Recognition and Attendance Management",
            font=ctk.CTkFont(
                size=18
            )
        )

        subtitle.pack(
            anchor="w",
            padx=25,
            pady=(0, 25)
        )

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=25,
            pady=20
        )

        recognition_btn = ctk.CTkButton(

            button_frame,

            text="🎥 Start Recognition",

            width=260,

            height=60,

            corner_radius=15,

            font=ctk.CTkFont(
                size=16,
                weight="bold"
            ),

            command=self.start_recognition

        )

        recognition_btn.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        attendance_btn = ctk.CTkButton(

            button_frame,

            text="📋 View Attendance",

            width=260,

            height=60,

            corner_radius=15

        )

        attendance_btn.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        search_btn = ctk.CTkButton(

            button_frame,

            text="🔍 Search Attendance",

            width=260,

            height=60,

            corner_radius=15

        )

        search_btn.grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        report_btn = ctk.CTkButton(

            button_frame,

            text="📄 Generate Report",

            width=260,

            height=60,

            corner_radius=15

        )

        report_btn.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        info_frame = ctk.CTkFrame(
            self,
            corner_radius=20,
            fg_color="#1F2937"
        )

        info_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            info_frame,
            text="Recognition Workflow",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        ctk.CTkLabel(
            info_frame,
            text=(
                "1. Register Person\n"
                "2. Capture Faces\n"
                "3. Start Recognition\n"
                "4. Attendance Recorded Automatically"
            ),
            justify="left",
            font=ctk.CTkFont(
                size=16
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def start_recognition(self):

        try:

            subprocess.Popen(
                [
                    sys.executable,
                    os.path.join(
                        PROJECT_ROOT,
                        "main.py"
                    )
                ]
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )