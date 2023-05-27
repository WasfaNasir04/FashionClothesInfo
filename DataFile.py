# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FashionGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import sorce_sc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1127, 790)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1541, 851))
        self.widget.setStyleSheet("background-color:rgb(226, 176, 255)\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(270, 10, 541, 41))
        self.label.setStyleSheet("font: 87 18pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 921, 421))
        self.label_2.setStyleSheet("image: url(:/pics/image.jpg)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self.widget)
        self.tableView.setGeometry(QtCore.QRect(90, 561, 921, 181))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.widget)

        self.model = QtGui.QStandardItemModel(self.tableView)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.comboBox.setGeometry(QtCore.QRect(400, 490, 301, 41))
        self.comboBox.setStyleSheet("font: 75 italic 14pt \"Arial\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 490, 281, 41))
        self.label_3.setStyleSheet("font: 63 18pt \"Yu Gothic UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(840, 540, 141, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(730, 490, 271, 41))
        self.comboBox_2.setStyleSheet("font: 75 italic 14pt \"Arial\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(120, 760, 871, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "*****Fashion Clothes Info*****"))
        self.comboBox.setItemText(0, _translate("Form", "Insertion Sort"))
        self.comboBox.setItemText(1, _translate("Form", "Selection Sort"))
        self.comboBox.setItemText(2, _translate("Form", "Bubble Sort"))
        self.comboBox.setItemText(3, _translate("Form", "Merge Sort"))
        self.comboBox.setItemText(4, _translate("Form", "Quick Sort"))
        self.comboBox.setItemText(5, _translate("Form", "Counting Sort"))
        self.comboBox.setItemText(6, _translate("Form", "Bucket Sort"))
        self.comboBox.setItemText(7, _translate("Form", "Radix Sort"))
        self.comboBox.setItemText(8, _translate("Form", "Heap Sort"))
        self.comboBox.setItemText(9, _translate("Form", "Slow Sort"))
        self.comboBox.setItemText(10, _translate("Form", "Cycle Sort"))
        self.comboBox.setItemText(11, _translate("Form", "Shell Sort"))
        self.comboBox.setItemText(12, _translate("Form", "Combo Sort"))
        self.comboBox.setItemText(13, _translate("Form", "Sleep Sort"))
        self.label_3.setText(_translate("Form", "SortingAlgorithms:"))
        self.comboBox_2.setItemText(0, _translate("Form", "Ascending Order"))
        self.comboBox_2.setItemText(1, _translate("Form", "Descending Order"))
    

    def loadCsv(self, Fashion):
        with open(Fashion, "r") as fileInput:
            for row in csv.reader(fileInput):    
                Data = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(Data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    path = r"F:\CS261F21PID56\FinalFolder\Fashion.csv"
    ui.loadCsv(path)
    sys.exit(app.exec_())
