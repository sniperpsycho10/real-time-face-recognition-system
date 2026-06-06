import customtkinter as ctk


class StatCard(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        title,
        value
    ):

        super().__init__(

            parent,

            width=300,

            height=180,

            corner_radius=25,

            fg_color="#1F2937"

        )

        self.pack_propagate(False)

        title_label = ctk.CTkLabel(

            self,

            text=title,

            font=ctk.CTkFont(

                size=20,

                weight="bold"

            )

        )

        title_label.pack(
            pady=(35, 10)
        )

        value_label = ctk.CTkLabel(

            self,

            text=value,

            font=ctk.CTkFont(

                size=42,

                weight="bold"

            )

        )

        value_label.pack()