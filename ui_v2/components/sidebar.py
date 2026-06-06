import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        app
    ):

        super().__init__(
            parent,
            width=320,
            corner_radius=0,
            fg_color="#111827"
        )

        self.app = app

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="⚡ Cyber Vision",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        title.pack(
            pady=(35, 40)
        )

        self.create_button(
            "🏠 Dashboard",
            self.app.show_dashboard
        )

        self.create_button(
            "👤 Users",
            self.app.show_users
        )

        self.create_button(
            "📋 Attendance",
            self.app.show_attendance
        )

        self.create_button(
            "📊 Analytics",
            self.app.show_analytics
        )

        self.create_button(
            "🚪 Exit",
            self.app.root.destroy
        )

    def create_button(
        self,
        text,
        command
    ):

        button = ctk.CTkButton(

            self,

            text=text,

            command=command,

            height=55,

            corner_radius=15,

            fg_color="#1F2937",

            hover_color="#2563EB",

            border_width=1,

            border_color="#374151",

            font=ctk.CTkFont(
                size=16,
                weight="bold"
            )

        )

        button.pack(
            fill="x",
            padx=20,
            pady=8
        )