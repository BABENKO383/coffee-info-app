import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi


class CoffeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, roast_level, ground_type, taste_description, 
                   price, package_volume 
            FROM coffee
        """)
        data = cursor.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels([
            'ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
            'Описание вкуса', 'Цена', 'Объем упаковки'
        ])

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())