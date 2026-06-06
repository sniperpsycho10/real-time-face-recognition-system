import customtkinter as ctk


class RecentActivity(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            corner_radius=20
        )

        ctk.CTkLabel(
            self,
            text="Recent Attendance",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        records = [
            "Ayush - 09:15",
            "APS - 09:20",
            "Aryan - 09:25"
        ]

        for record in records:

            ctk.CTkLabel(
                self,
                text=record,
                font=("Arial", 16)
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )