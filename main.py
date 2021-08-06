# Written by Sean Kyer, 2021 at Metro Printers

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileMerger
from PyPDF2 import pdf

page_size_dict = {
    "letter": [612, 792],
    "legal": [612, 1008],
    "max": [14400, 14400]
}


def n_up(fp, n_across, n_down, x_gutter, y_gutter, page_size, one_page):
    reader = PdfFileReader(open(fp, 'rb'))  # Open target file

    num_of_pages = reader.getNumPages()

    # Obtain information based on first page of PDF file (script assumes MediaBox is consistent throughout pages)
    page0 = reader.getPage(0)
    page0_h = page0.mediaBox.getHeight()
    page0_w = page0.mediaBox.getWidth()

    # creates page dimensions based on desired size
    if one_page:
        new_page_w = page0_w * n_across
        new_page_h = page0_h * n_down
    else:
        new_page_w = page_size_dict[page_size][0]
        new_page_h = page_size_dict[page_size][1]

    new_pdf_pages = []
    new_pdf_page = pdf.PageObject.createBlankPage(None, new_page_w, new_page_h)  # Create new page

    column_count = 1  # Row counter

    for i in range(num_of_pages):
        next_page = reader.getPage(i)
        print("X coordinate: " + str((i % n_across) * page0_w))
        print("Y coordinate: " + str(column_count * page0_h))

        new_pdf_page.mergeScaledTranslatedPage(next_page,
                                               1,
                                               ((i % n_across) * page0_w) + ((i % n_across) * x_gutter),
                                               new_page_h - (column_count * page0_h) - (y_gutter * (column_count - 1)),
                                               one_page
                                               )

        # When you get to the end of a row, move to next column
        if i % n_across == n_across - 1:
            column_count += 1

    # Combine all pages and write file
    writer = PdfFileWriter()

    writer.addPage(new_pdf_page)

    # for page in new_pdf_pages:
    #    writer.addPage(page)

    with open("output.pdf", 'wb') as f:
        writer.write(f)


if __name__ == "__main__":
    path = "example.pdf"
    n_up(path, 2, 4, 72, 72, "legal", False)
