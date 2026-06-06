import customtkinter as ctk


class AnalyticsPage(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#111827"
        )

        title = ctk.CTkLabel(
            self,
            text="Analytics",
            font=ctk.CTkFont(
                size=40,
                weight="bold"
            )
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=25
        )