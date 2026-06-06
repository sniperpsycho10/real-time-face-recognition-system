import pandas as pd


def generate_report():

    try:

        df = pd.read_csv(
            "logs/attendance.csv"
        )

    except Exception as error:

        print(
            f"Error: {error}"
        )

        return

    report = ""

    report += (
        "\n===== ATTENDANCE REPORT =====\n\n"
    )

    report += (
        f"Total Records : {len(df)}\n"
    )

    report += (
        f"Unique People : "
        f"{df['Name'].nunique()}\n\n"
    )

    report += (
        "Attendance Count:\n"
    )

    report += (
        str(
            df["Name"]
            .value_counts()
        )
    )

    report += "\n\n"

    report += (
        "Attendance By Date:\n"
    )

    report += (
        str(
            df["Date"]
            .value_counts()
        )
    )

    report += "\n\n"

    most_active = (
        df["Name"]
        .value_counts()
        .idxmax()
    )

    report += (
        f"Most Active User : "
        f"{most_active}\n"
    )

    print(report)

    with open(
        "logs/attendance_report.txt",
        "w"
    ) as file:

        file.write(
            report
        )

    print(
        "\nReport Saved:"
    )

    print(
        "logs/attendance_report.txt"
    )


if __name__ == "__main__":

    generate_report()