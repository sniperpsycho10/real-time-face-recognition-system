import customtkinter as ctk

from components.sidebar import Sidebar

from pages.dashboard_page import DashboardPage

from pages.users_page import UsersPage

from pages.attendance_page import AttendancePage

from pages.analytics_page import AnalyticsPage


class App:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title(
            "Cyber Vision"
        )

        self.root.geometry(
            "1800x1000"
        )

        self.root.minsize(
            1400,
            900
        )

        self.build_ui()

    def build_ui(self):

        self.sidebar = Sidebar(
            self.root,
            self
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.content_frame = ctk.CTkFrame(
            self.root,
            fg_color="#111827"
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.show_dashboard()

    def clear_content(self):

        for widget in self.content_frame.winfo_children():

            widget.destroy()

    def show_dashboard(self):

        self.clear_content()

        DashboardPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )

    def show_users(self):

        self.clear_content()

        UsersPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )

    def show_attendance(self):

        self.clear_content()

        AttendancePage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )

    def show_analytics(self):

        self.clear_content()

        AnalyticsPage(
            self.content_frame
        ).pack(
            fill="both",
            expand=True
        )

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    app = App()

    app.run()