# Written by Sean Kyer, 2021 at Metro Printers

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, pdf


def n_up(path, across, down, x_gutter, y_gutter):
    reader = PdfFileReader(open(path, 'rb')) # Open target file

    NUM_OF_PAGES = reader.getNumPages()

    # Obtain information based on first page of PDF file (script assumes MediaBox is consistent throughout pages)
    page0 = reader.getPage(0)
    page0_h = page0.mediaBox.getHeight()
    page0_w = page0.mediaBox.getWidth()

    # !!! TEMP, but essentially is creating the width and height of the new page
    newPage_h = page0_h * down
    newPage_w = page0_w * across

    newpdf_pages = []
    newpdf_page = pdf.PageObject.createBlankPage(None, newPage_w, newPage_h) # Create new page

    column_count = 1 # Row counter

    for i in range(NUM_OF_PAGES):
        next_page = reader.getPage(i)
        print("X coordinate: ")
        print((i % across) * page0_w)
        print("Y coordinate: ")
        print(column_count * page0_h)

        if i % across == 0:
            x_gut = 0
        else:
            x_gut = x_gutter

        if (i % across) < across - 1:
            y_gut = 0
        else:
            y_gut = y_gutter

        newpdf_page.mergeScaledTranslatedPage(next_page,
                                              1,
                                              ((i % across) * page0_w) + x_gut,
                                              (column_count * page0_h) + y_gut,
                                              True
                                              )

        # When you get to the end of a row, move to next column
        if i % across == across - 1:
            column_count += 1


    # Combine all pages and write file
    writer = PdfFileWriter()

    for page in newpdf_pages:
        writer.addPage(newpdf_page)

    with open("output.pdf", 'wb') as f:
        writer.write(f)


if __name__ == "__main__":
    path = "example.pdf"
    n_up(path, 2, 4, 72, 72)
