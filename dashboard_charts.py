import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg as FigureCanvasTKAgg
)
import tkinter as tk
def show_dashboard():
    root=tk.Tk()
    root.title("Attendance analytics")
    root.geometry("1200x700")
    df=pd.read_csv("logs/attendance.csv")
    attendance_count=(df["Name"].value_counts())
    figure=plt.Figure(figsize=(8,5),dpi=100)
    axis=figure.add_subplot(111)
    attendance_count.plot(kind="bar",ax=axis)
    axis.set_title("attendance count per person")
    canvas = FigureCanvasTKAgg(figure, root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both",expand=True)
    root.mainloop()
if __name__=="__main__":
    show_dashboard()