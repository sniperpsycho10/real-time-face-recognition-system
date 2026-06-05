import pandas as pd


def main():

    try:

        df = pd.read_csv(
            "logs/attendance.csv"
        )

    except FileNotFoundError:

        print(
            "Attendance file not found."
        )

        return

    print(
        "\n===== ATTENDANCE REPORT =====\n"
    )

    print(df)

    print(
        "\n===== STATISTICS =====\n"
    )

    print(
        f"Total Records: {len(df)}"
    )

    print(
        f"Unique People: {df['Name'].nunique()}"
    )

    print(
        "\nAttendance Count:\n"
    )

    print(
        df["Name"]
        .value_counts()
    )


if __name__ == "__main__":
    main()