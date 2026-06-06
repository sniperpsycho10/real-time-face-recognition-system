import customtkinter as ctk


class StatusWidget(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            corner_radius=20
        )

        ctk.CTkLabel(
            self,
            text="System Status",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=20
        )

        statuses = [
            "🟢 Database Connected",
            "🟢 Camera Available",
            "🟢 Recognition Ready"
        ]

        for status in statuses:

            ctk.CTkLabel(
                self,
                text=status,
                font=("Arial", 16)
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )