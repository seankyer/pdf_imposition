#!/usr/local/bin/python3

# Written by Sean Kyer, 2021 at Metro Printers
# github.com/seankyer/pdf_imposition

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import pdf

import math
import time

# Page size catalogue
page_size_dict = {
    "letter": [612, 792],
    "legal": [612, 1008],
    "max": [14400, 14400]
}


def inch_to_pt(inches):
    return inches * 72


def n_up(fp, n_across, n_down, x_gut, y_gut, page_size, is_one_page):
    reader = PdfFileReader(open(fp, 'rb'))  # Open target file
    print("Page count for fp: " + str(reader.getNumPages()))
    x_gutter = inch_to_pt(x_gut)
    y_gutter = inch_to_pt(y_gut)

    # Obtain information based on first page of PDF file (script assumes MediaBox is consistent throughout pages)
    page0_h = reader.getPage(0).mediaBox.getHeight()
    page0_w = reader.getPage(0).mediaBox.getWidth()

    # creates page dimensions based on desired size
    if is_one_page:
        new_page_w = (page0_w * n_across) + ((n_across - 1) * x_gutter) + inch_to_pt(1)  # +1 inch for buffer
        new_page_h = (page0_h * n_down) + ((n_down - 1) * y_gutter)
    else:
        new_page_w = page_size_dict[page_size][0]
        new_page_h = page_size_dict[page_size][1]

    # Sanity checks
    if ((page0_w * n_across) + ((n_across - 1) * x_gutter)) > new_page_w:
        print("n_across too large for desired canvas")
        return -1
    if ((page0_h * n_down) + ((n_down - 1) * y_gutter)) > new_page_h:
        print("n_down too large for desired canvas")
        return -1

    new_pdf_page_count = math.ceil(reader.getNumPages() / (n_across * n_down))

    new_pdf_pages = []
    for n in range(new_pdf_page_count):
        new_pdf_page = pdf.PageObject.createBlankPage(None, new_page_w, new_page_h)  # Create new page
        new_pdf_pages.append(new_pdf_page)

    column_count = 1  # Row counter
    page_count = 0    # page count

    # Arithmetic to center elements on the x axis
    x_pos_start = (new_page_w - ((n_across * page0_w) + ((n_across - 1) * x_gutter))) / 2
    y_pos_start = (new_page_h - ((n_down * page0_h) + ((n_down - 1) * y_gutter))) / 2

    for n in range(0, reader.getNumPages()):
        next_page = reader.getPage(n)
        new_pdf_pages[page_count].mergeScaledTranslatedPage(next_page,
                                                       1,

                                                       x_pos_start +
                                                       ((n % n_across) * page0_w) +
                                                       ((n % n_across) * x_gutter),

                                                       new_page_h -
                                                       y_pos_start -
                                                       (column_count * page0_h) -
                                                       (y_gutter * (column_count - 1)),

                                                       is_one_page
                                                       )

        if n % n_across == n_across - 1:
            column_count += 1

        if (n + 1) % (n_across * n_down) == 0:
            page_count += 1
            column_count = 0

    # Combine all pages and write file
    writer = PdfFileWriter()

    for page in new_pdf_pages:
        writer.addPage(page)

    with open("output.pdf", 'wb') as f:
        writer.write(f)

    print("output.pdf exported")
    return 0


if __name__ == "__main__":
    path = "example.pdf"
    n_up(path, 2, 3, 0, 0, "letter", False)
