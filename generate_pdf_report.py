from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from src.database_manager import (
    DatabaseManager
)

import os


def generate_report():

    os.makedirs(
        "reports",
        exist_ok=True
    )

    pdf_path = (
        "reports/attendance_report.pdf"
    )

    document = SimpleDocTemplate(
        pdf_path
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "Attendance Report",
        styles["Title"]
    )

    content.append(
        title
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    database = (
        DatabaseManager()
    )

    records = (
        database.fetch_all_records()
    )

    data = [
        [
            "ID",
            "Name",
            "Date",
            "Time"
        ]
    ]

    for record in records:

        data.append(
            list(record)
        )

    table = Table(
        data
    )

    table.setStyle(
        TableStyle(
            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.grey
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.whitesmoke
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

            ]
        )
    )

    content.append(
        table
    )

    document.build(
        content
    )

    database.close()

    print(
        f"\nReport Generated:\n{pdf_path}"
    )


if __name__ == "__main__":

    generate_report()