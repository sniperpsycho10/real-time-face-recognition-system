import customtkinter as ctk

from components.stat_card import (
    StatCard
)

from components.recent_activity import (
    RecentActivity
)

from components.status_widget import (
    StatusWidget
)


class DashboardPage(
    ctk.CTkFrame
):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent,
            fg_color="#111827"
        )

        # Title

        title = ctk.CTkLabel(

            self,

            text="Dashboard",

            font=ctk.CTkFont(

                size=40,

                weight="bold"

            )

        )

        title.pack(

            anchor="w",

            padx=25,

            pady=(20, 10)

        )

        # Hero Section

        hero = ctk.CTkFrame(

            self,

            height=140,

            corner_radius=25,

            fg_color="#1F2937"

        )

        hero.pack(

            fill="x",

            padx=25,

            pady=15

        )

        hero.pack_propagate(False)

        ctk.CTkLabel(

            hero,

            text="Welcome to Cyber Vision",

            font=ctk.CTkFont(

                size=28,

                weight="bold"

            )

        ).pack(

            anchor="w",

            padx=30,

            pady=(25, 5)

        )

        ctk.CTkLabel(

            hero,

            text="Monitor attendance and analytics in real time.",

            font=ctk.CTkFont(

                size=16

            )

        ).pack(

            anchor="w",

            padx=30

        )

        # Cards Row

        cards_frame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        cards_frame.pack(

            fill="x",

            padx=25,

            pady=15

        )

        StatCard(

            cards_frame,

            "👤 Users",

            "3"

        ).pack(

            side="left",

            padx=10

        )

        StatCard(

            cards_frame,

            "📋 Records",

            "25"

        ).pack(

            side="left",

            padx=10

        )

        StatCard(

            cards_frame,

            "📅 Today",

            "4"

        ).pack(

            side="left",

            padx=10

        )

        StatCard(

            cards_frame,

            "🎯 Accuracy",

            "97%"

        ).pack(

            side="left",

            padx=10

        )

        # Bottom Area

        bottom_frame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        bottom_frame.pack(

            fill="both",

            expand=True,

            padx=25,

            pady=20

        )

        recent = RecentActivity(
            bottom_frame
        )

        recent.pack(

            side="left",

            fill="both",

            expand=True,

            padx=10

        )

        status = StatusWidget(
            bottom_frame
        )

        status.pack(

            side="left",

            fill="both",

            expand=True,

            padx=10

        )