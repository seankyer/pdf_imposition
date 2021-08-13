#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'n_up_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os

from PyQt5 import QtCore, QtGui, QtWidgets

PAGE_SIZES = ["letter", "legal", "max"]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Target_file_title = QtWidgets.QLineEdit(self.centralwidget)
        self.Target_file_title.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.Target_file_title.setReadOnly(True)
        self.Target_file_title.setObjectName("Target_file_title")
        self.Target_file_text_box = QtWidgets.QLineEdit(self.centralwidget)
        self.Target_file_text_box.setGeometry(QtCore.QRect(90, 10, 151, 21))
        self.Target_file_text_box.setReadOnly(True)
        self.Target_file_text_box.setObjectName("Target_file_text_box")
        self.N_across_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.N_across_spinbox.setGeometry(QtCore.QRect(140, 60, 42, 22))
        self.N_across_spinbox.setSuffix("")
        self.N_across_spinbox.setMinimum(1)
        self.N_across_spinbox.setMaximum(999999)
        self.N_across_spinbox.setObjectName("n_across_spinbox")
        self.N_down_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.N_down_spinbox.setGeometry(QtCore.QRect(140, 90, 42, 22))
        self.N_down_spinbox.setMinimum(1)
        self.N_down_spinbox.setMaximum(99999)
        self.N_down_spinbox.setObjectName("N_down_spinbox")
        self.X_gutter_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.X_gutter_spinbox.setGeometry(QtCore.QRect(140, 130, 62, 22))
        self.X_gutter_spinbox.setObjectName("X_gutter_spinbox")
        self.Y_gutter_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.Y_gutter_spinbox.setGeometry(QtCore.QRect(140, 160, 62, 22))
        self.Y_gutter_spinbox.setObjectName("Y_gutter_spinbox")
        self.Page_size_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.Page_size_dropdown.setGeometry(QtCore.QRect(100, 200, 171, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Page_size_dropdown.sizePolicy().hasHeightForWidth())
        self.Page_size_dropdown.setSizePolicy(sizePolicy)
        self.Page_size_dropdown.setObjectName("Page_size_dropdown")
        self.Page_size_dropdown.addItem("")
        self.Page_size_dropdown.addItem("")
        self.Page_size_dropdown.addItem("")
        self.Fit_page_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Fit_page_checkbox.setGeometry(QtCore.QRect(10, 240, 271, 20))
        self.Fit_page_checkbox.setObjectName("Fit_page_checkbox")
        self.Impose_button = QtWidgets.QPushButton(self.centralwidget)
        self.Impose_button.setGeometry(QtCore.QRect(80, 270, 113, 32))
        self.Impose_button.setDefault(False)
        self.Impose_button.setObjectName("Impose_button")
        self.N_across_title = QtWidgets.QLineEdit(self.centralwidget)
        self.N_across_title.setGeometry(QtCore.QRect(10, 60, 113, 21))
        self.N_across_title.setReadOnly(True)
        self.N_across_title.setObjectName("N_across_title")
        self.N_down_title = QtWidgets.QLineEdit(self.centralwidget)
        self.N_down_title.setGeometry(QtCore.QRect(10, 90, 113, 21))
        self.N_down_title.setReadOnly(True)
        self.N_down_title.setObjectName("N_down_title")
        self.X_gutter_title = QtWidgets.QLineEdit(self.centralwidget)
        self.X_gutter_title.setGeometry(QtCore.QRect(10, 130, 113, 21))
        self.X_gutter_title.setReadOnly(True)
        self.X_gutter_title.setObjectName("X_gutter_title")
        self.Y_gutter_title = QtWidgets.QLineEdit(self.centralwidget)
        self.Y_gutter_title.setGeometry(QtCore.QRect(10, 160, 113, 21))
        self.Y_gutter_title.setReadOnly(True)
        self.Y_gutter_title.setObjectName("Y_gutter_title")
        self.Page_size_title = QtWidgets.QLineEdit(self.centralwidget)
        self.Page_size_title.setGeometry(QtCore.QRect(10, 200, 81, 21))
        self.Page_size_title.setReadOnly(True)
        self.Page_size_title.setObjectName("Page_size_title")
        self.Error_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.Error_textbox.setGeometry(QtCore.QRect(0, 300, 271, 41))
        self.Error_textbox.setFrame(True)
        self.Error_textbox.setReadOnly(True)
        self.Error_textbox.setObjectName("Error_textbox")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Target_file_title.setText(_translate("MainWindow", "Target File:"))
        self.Target_file_text_box.setText(_translate("MainWindow", "Temp Name"))
        self.Page_size_dropdown.setItemText(0, _translate("MainWindow", "Letter (8.5x11\")"))
        self.Page_size_dropdown.setItemText(1, _translate("MainWindow", "Legal (8.5x14\")"))
        self.Page_size_dropdown.setItemText(2, _translate("MainWindow", "Maximum (200x200\")"))
        self.Fit_page_checkbox.setText(_translate("MainWindow", "Fit to one page? (Ignores N-down)"))
        self.Impose_button.setText(_translate("MainWindow", "Impose"))
        self.N_across_title.setText(_translate("MainWindow", "N-across:"))
        self.N_down_title.setText(_translate("MainWindow", "N-down:"))
        self.X_gutter_title.setText(_translate("MainWindow", "X-Gutter:"))
        self.Y_gutter_title.setText(_translate("MainWindow", "Y-Gutter:"))
        self.Page_size_title.setText(_translate("MainWindow", "Page Size:"))
        self.Error_textbox.setText(_translate("MainWindow", ""))

        # Function Hookup
        self.Impose_button.clicked.connect(self.call_n_up)
        self.Target_file_text_box.setText(os.path.basename(droppedFile))

    def call_n_up(self):
        print(self.N_across_spinbox.text())
        print(self.N_down_spinbox.text())
        print(self.X_gutter_spinbox.text())
        print(self.Y_gutter_spinbox.text())
        print(self.Page_size_dropdown.currentIndex())
        print(self.Fit_page_checkbox.isChecked())
        code = n_up_fun(droppedFile,
                        int(self.N_across_spinbox.text()),
                        int(self.N_down_spinbox.text()),
                        int(self.X_gutter_spinbox.text()),
                        int(self.Y_gutter_spinbox.text()),
                        PAGE_SIZES[self.Page_size_dropdown.currentIndex()],
                        self.Fit_page_checkbox.isChecked())
        self.Error_textbox.setText(code)


from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
from PyPDF2 import pdf

import math

# Page size catalogue
page_size_dict = {
    "letter": [612, 792],
    "legal": [612, 1008],
    "max": [14400, 14400]
}


def inch_to_pt(inches):
    return inches * 72


def n_up_fun(fp, n_across, n_down, x_gut, y_gut, page_size, is_one_page):
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
        return "n_across too large for desired canvas"
    if ((page0_h * n_down) + ((n_down - 1) * y_gutter)) > new_page_h:
        return "n_down too large for desired canvas"

    new_pdf_page_count = math.ceil(reader.getNumPages() / (n_across * n_down))

    new_pdf_pages = []
    for n in range(new_pdf_page_count):
        new_pdf_page = pdf.PageObject.createBlankPage(None, new_page_w, new_page_h)  # Create new page
        new_pdf_pages.append(new_pdf_page)

    column_count = 1  # Row counter
    page_count = 0  # page count

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
            column_count = 1

    # Combine all pages and write file
    writer = PdfFileWriter()

    for page in new_pdf_pages:
        writer.addPage(page)

    with open("/Users/prepress-2/Desktop/output.pdf", 'wb') as f:
        writer.write(f)

    print("output.pdf exported")
    return "success"


if __name__ == "__main__":
    import sys

    droppedFile = sys.argv[1]
    #droppedFile = "example.pdf"
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
