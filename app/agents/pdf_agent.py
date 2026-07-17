from fpdf import FPDF
from datetime import datetime


def create_wellness_pdf(
    mood,
    journal,
    sleep,
    meditation
):

    pdf = FPDF()

    pdf.add_page()

    # Title
    pdf.set_font(
        "Arial",
        "B",
        18
    )

    pdf.cell(
        0,
        10,
        "MindCare AI Wellness Report",
        ln=True,
        align="C"
    )

    pdf.ln(5)

    # Date
    pdf.set_font(
        "Arial",
        size=11
    )

    pdf.cell(
        0,
        10,
        f"Generated on: {datetime.now().strftime('%Y-%m-%d')}",
        ln=True
    )

    pdf.ln(10)


    def add_section(title, content):

        pdf.set_font(
            "Arial",
            "B",
            13
        )

        pdf.cell(
            0,
            10,
            title,
            ln=True
        )

        pdf.set_font(
            "Arial",
            size=11
        )

        pdf.multi_cell(
            0,
            8,
            str(content)
        )

        pdf.ln(5)


    add_section(
        "🧠 Mood Analysis",
        mood
    )

    add_section(
        "📖 Journal Reflection",
        journal
    )

    add_section(
        "😴 Sleep Analysis",
        sleep
    )

    add_section(
        "🧘 Meditation Recommendation",
        meditation
    )


    file_name = "MindCare_Wellness_Report.pdf"

    pdf.output(
        file_name
    )

    return file_name