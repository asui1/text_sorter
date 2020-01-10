

import sys
from PyQt5.QtWidgets import *


open_file_at = ""
alpha_order = True
check_mis = False
save_file_at = ""

class text_sorter_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Text Sorter")

        #파일 받아오기
        self.pushButton = QPushButton("Open File", self)
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLineEdit()

        #오타 따로 모으는지에 대한 checkbox
        self.error_checkbox = QCheckBox("Check Possible Mis-spellings Separately?")
        self.error_checkbox.adjustSize()
        self.error_checkbox.setChecked(False)

        #사용 횟수/알파벳 순서에 따른 정렬
        self.alpha_tog = QPushButton("Alphabetical Order")
        self.alpha_tog.setCheckable(True)
        self.alpha_tog.setChecked(True)
        self.alpha_tog.adjustSize()
        self.alpha_tog.clicked[bool].connect(self.toggleOrder)
        self.freq_tog = QPushButton("Frequency Order")
        self.freq_tog.setCheckable(True)
        self.freq_tog.adjustSize()
        self.freq_tog.clicked[bool].connect(self.toggleOrder)

        #저장경로 정하기
        self.save_button = QPushButton("Save at", self)
        self.save_button.clicked.connect(self.saveButtonClicked)
        self.save_label = QLineEdit()

        #실행 버튼
        self.run_button = QPushButton("RUN")
        self.run_button.clicked.connect(self.printCheck)

        #layout
        grid.addWidget(self.pushButton, 0, 1)
        grid.addWidget(self.label, 0, 0)
        hbox = QHBoxLayout()
        hbox.addWidget(self.alpha_tog)
        hbox.addWidget(self.freq_tog)
        grid.addLayout(hbox, 1, 0)
        grid.addWidget(self.error_checkbox, 2, 0)
        grid.addWidget(self.save_button, 3, 1)
        grid.addWidget(self.save_label, 3, 0)
        grid.addWidget(self.run_button, 5, 1)
        self.setLayout(grid)

    def printCheck(self):
        open_file_at = self.label.text()
        alpha_order = self.alpha_tog.isChecked()
        check_mis = self.error_checkbox.isChecked()
        save_file_at = self.save_label.text()
        if open_file_at == "" or save_file_at == "":
            QMessageBox.about(self, "Warning", "파일을 선택하지 않았습니다.")
        else:
            pass

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "Text Files(*.txt);; All Files(*)", '/home')
        self.label.setText(fname[0])

    def toggleOrder(self):
        order = self.sender()

        if order.text() == "Frequency Order":
            self.alpha_tog.setChecked(False)
        else:
            self.freq_tog.setChecked(False)

    def saveButtonClicked(self):
        gname = QFileDialog.getSaveFileName(self, 'Save File As', "", "Excel Files(*.xlsx);; All Files(*)", '/home')
        self.save_label.setText(gname[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    w = size.width()/4
    h = size.height()/3
    ex = text_sorter_UI()
    ex.show()
    ex.setGeometry(size.width()/2 - w/2, size.height()/2-h/2, w, h)

    sys.exit(app.exec_())


