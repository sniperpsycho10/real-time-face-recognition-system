import customtkinter as ctk

from tkinter import (
    messagebox,
    simpledialog
)

import os
import sys


# Allow imports from project root

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


from capture_faces import capture_faces


class UsersPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#111827"
        )

        self.project_root = PROJECT_ROOT

        title = ctk.CTkLabel(
            self,
            text="Users Management",
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
            text="Register users and collect training images",
            font=ctk.CTkFont(
                size=18
            )
        )

        subtitle.pack(
            anchor="w",
            padx=25,
            pady=(0, 25)
        )

        # Main Button Frame

        button_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        button_frame.pack(
            anchor="w",
            padx=25,
            pady=20
        )

        register_btn = ctk.CTkButton(

            button_frame,

            text="👤 Register Person",

            width=250,

            height=60,

            corner_radius=15,

            font=ctk.CTkFont(
                size=16,
                weight="bold"
            ),

            command=self.register_person

        )

        register_btn.grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        capture_btn = ctk.CTkButton(

            button_frame,

            text="📸 Capture Faces",

            width=250,

            height=60,

            corner_radius=15,

            font=ctk.CTkFont(
                size=16,
                weight="bold"
            ),

            command=self.capture_faces_gui

        )

        capture_btn.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Info Box

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
            text="Workflow",
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
            text="1. Register Person\n2. Capture Faces\n3. Start Recognition",
            justify="left",
            font=ctk.CTkFont(
                size=16
            )
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def register_person(self):

        person_name = simpledialog.askstring(
            "Register Person",
            "Enter Person Name:"
        )

        if not person_name:

            return

        folder_path = os.path.join(
            self.project_root,
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
            folder_path,
            exist_ok=True
        )

        messagebox.showinfo(
            "Success",
            f"{person_name} registered successfully."
        )

    def capture_faces_gui(self):

        person_name = simpledialog.askstring(
            "Capture Faces",
            "Enter Person Name:"
        )

        if not person_name:

            return

        folder_path = os.path.join(
            self.project_root,
            "data",
            "known_faces",
            person_name.strip()
        )

        if not os.path.exists(
            folder_path
        ):

            messagebox.showerror(
                "Error",
                f"{person_name} is not registered."
            )

            return

        try:

            capture_faces(
                person_name.strip()
            )

            messagebox.showinfo(
                "Success",
                "Face capture completed.\nDatabase updated."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )