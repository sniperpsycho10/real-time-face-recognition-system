import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf():

    try:

        df = pd.read_csv(
            "logs/attendance.csv"
        )

    except Exception as error:

        print(error)

        return

    pdf = SimpleDocTemplate(
        "reports/attendance_report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Attendance Report",
        styles["Title"]
    )

    elements.append(
        title
    )

    elements.append(
        Spacer(1, 12)
    )

    total_records = len(df)

    unique_people = (
        df["Name"]
        .nunique()
    )

    elements.append(
        Paragraph(
            f"Total Records : {total_records}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Unique People : {unique_people}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    attendance_count = (
        df["Name"]
        .value_counts()
    )

    elements.append(
        Paragraph(
            "Attendance Count:",
            styles["Heading2"]
        )
    )

    for name, count in attendance_count.items():

        elements.append(
            Paragraph(
                f"{name} : {count}",
                styles["Normal"]
            )
        )

    pdf.build(
        elements
    )

    print(
        "PDF Report Generated"
    )


if __name__ == "__main__":

    generate_pdf()