import pandas as pd
import matplotlib.pyplot as plt


def main():

    try:

        df = pd.read_csv(
            "logs/attendance.csv"
        )

    except Exception as error:

        print(error)

        return

    attendance_count = (
        df["Name"]
        .value_counts()
    )

    date_count = (
        df["Date"]
        .value_counts()
    )

    plt.figure(
        figsize=(10, 6)
    )

    attendance_count.plot(
        kind="bar"
    )

    plt.title(
        "Attendance Count Per Person"
    )

    plt.xlabel(
        "Person"
    )

    plt.ylabel(
        "Attendance Count"
    )

    plt.tight_layout()

    plt.show()
    plt.figure(
        figsize=(10, 6)
    )       

    date_count.plot(
        kind="bar"
    )

    plt.title(
        "Attendance By Date"
    )

    plt.xlabel(
        "Date"
    )

    plt.ylabel(
        "Records"
    )

    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()