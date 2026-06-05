import pandas as pd
def main():
    df = pd.read_csv(
        "logs/attendance.csv"
    )
    print(
        "\n===== ANALYTICS =====\n"
    )
    print(
        f"Total Attendance Records : {len(df)}"
    )
    print(
        f"Unique People : {df['Name'].nunique()}"
    )
    print(
        "\nAttendance Count:\n"
    )
    print(
        df["Name"]
        .value_counts()
    )
    print(
        "\nAttendance By Date:\n"
    )
    print(
        df["Date"]
        .value_counts()
    )
if __name__ == "__main__":
    main()