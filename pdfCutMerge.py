import os
from PyPDF2 import PdfReader, PdfWriter

PDF_FOLDER = r"C:\\Users\\.."


def process_pdfs():
    writer = PdfWriter()

    for file in sorted(os.listdir(PDF_FOLDER)):
        if file.lower().endswith(".pdf"):
            reader = PdfReader(os.path.join(PDF_FOLDER, file))
            if len(reader.pages) > 2:
                for page in range(1, len(reader.pages) - 1):
                    writer.add_page(reader.pages[page])

    with open(os.path.join(PDF_FOLDER, "merged_output.pdf"), "wb") as output:
        writer.write(output)


process_pdfs()
