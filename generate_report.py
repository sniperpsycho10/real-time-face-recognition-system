import pandas as pd

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


def export_csv(df):

    df.to_csv(
        "reports/attendance_export.csv",
        index=False
    )

    print(
        "CSV Export Complete"
    )


def export_pdf(df):

    pdf = SimpleDocTemplate(
        "reports/attendance_report.pdf"
    )

    styles = (
        getSampleStyleSheet()
    )

    elements = []

    title = Paragraph(
        "Attendance Report",
        styles["Title"]
    )

    elements.append(
        title
    )

    elements.append(
        Spacer(
            1,
            20
        )
    )

    data = [list(df.columns)]

    data.extend(
        df.values.tolist()
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
                )
            ]
        )
    )

    elements.append(
        table
    )

    pdf.build(
        elements
    )

    print(
        "PDF Export Complete"
    )


def main():

    try:

        df = pd.read_csv(
            "logs/attendance.csv"
        )

    except Exception as error:

        print(error)

        return

    export_csv(
        df
    )

    export_pdf(
        df
    )


if __name__ == "__main__":

    main()