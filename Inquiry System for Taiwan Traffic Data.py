import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import gui
from PyQt5 import QtCore, Qt
from logical import *


class window(QWidget, gui.Ui_Form):
    def __init__(self):
        super(window, self).__init__()
        self.setupUi(self)
        self.traffic_data = pd.read_csv("TDCS_M06A_20190830_080000.csv", header=None)
        self.pushButton.clicked.connect(self.demo)
        self.pushButton_2.clicked.connect(self.textBrowser.clear)
        self.pushButton_3.clicked.connect(self.search_gui)
        self.names = ['VehicleType', 'DerectionTime_O', 'GantryID_O', 'DerectionTime_D', 'GantryID_D', 'TripLength',
                      'TripEnd',
                      'TripInformation']
        self.traffic_data.columns = self.names
        self.traffic_data.head()
        self.sort_name = [inerstion_sort, bubble, merge_sort, quick_sort, heap, BST_sort, AVL_sort]
        self.VehicleType_manage = [row[0] for row in self.traffic_data.values.tolist()][:]
        self.DirectionTime_O_manage = [row[1] for row in self.traffic_data.values.tolist()][:]
        self.GantryID_O_manage = [row[2] for row in self.traffic_data.values.tolist()][:]

    def demo(self):
        index_0 = self.comboBox.currentIndex()
        index_1 = self.comboBox_3.currentIndex()
        result = sort_result(data=self.traffic_data, func=self.sort_name[index_0], col=self.names[index_1], size=0.005)
        self.textBrowser.append(str(result))

    def search_gui(self):
        index = self.comboBox_4.currentIndex()
        if self.lineEdit.text() == '':
            QMessageBox.information(self, "Warning", "The input cannot be empty！")
        else:
            data = [self.VehicleType_manage, self.DirectionTime_O_manage, self.GantryID_O_manage]
            result = search(self.traffic_data, self.lineEdit.text(), data[index])
            self.textBrowser.append(str(result))

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(Qt.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec_())
