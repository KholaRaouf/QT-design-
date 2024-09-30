import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow,QMessageBox, QApplication, QTableWidgetItem
from PyQt5 import QtCore
import csv

class Project(QMainWindow):
    def __init__(self):
        super(Project, self).__init__()
        loadUi("E:\\study\\Semester 3\\DSA lab\\week4 QT\\proj.ui", self) 

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.MinimizeButton.clicked.connect(lambda: self.showMinimized())
        self.CrossButton.clicked.connect(lambda: self.close())
        self.pushButton_sort.clicked.connect(self.show_selected_value)
        self.data = [] 
        self.load_table()
        self.tableWidget.cellClicked.connect(self.show_full_data)
        self.pushButton_search.clicked.connect(self.search_table)
        
    def show_full_data(self, row, column):

        cell_data = self.tableWidget.item(row, column).text()
        self.TextBox.setText(cell_data)

    def update_table(self, data):
        self.tableWidget.setRowCount(0)
        for row in data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column_index, item in enumerate(row):
                self.tableWidget.setItem(row_position, column_index, QTableWidgetItem(item))

    def search_table(self):
        search_text = self.lineEdit.text().lower() 
        filtered_data = [row for row in self.data if any(search_text in str(item).lower() for item in row)]
        if filtered_data:
            self.update_table(filtered_data)
        else: 
            self.tableWidget.setRowCount(0) 
       
    def load_table(self):
        try:
            with open("E:\\study\\Semester 3\\DSA lab\\week4 QT\\products.csv", "r", encoding="utf-8") as fileInput:
                self.data = list(csv.reader(fileInput))
                self.tableWidget.setRowCount(len(self.data))
                self.tableWidget.setColumnCount(len(self.data[0]))  
                for row_index, row_data in enumerate(self.data):
                    for column_index, column_data in enumerate(row_data):
                        self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(column_data))
        except FileNotFoundError:
            print("CSV file not found. Please check the file path.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def show_selected_value(self):
        selected_value = self.comboBox_algo.currentText() 
        self.show_message_box("Selected Value", f"You selected: {selected_value}")

    def show_message_box(self, title, message):
        msg_box = QMessageBox() 
        msg_box.setIcon(QMessageBox.Warning) 
        msg_box.setWindowTitle(title) 
        msg_box.setText(message) 
        msg_box.setStandardButtons(QMessageBox.Ok) 
        msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Project()
    window.show()
    sys.exit(app.exec_())