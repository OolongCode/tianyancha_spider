import sys
import pandas as pd
from my_Data import *
from my_Graph import my_graph
from my_Word import word_cut
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from my_Spider import my_spider_run,my_spider_init
from PyQt5.Qt import QThread, pyqtSignal


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(20, 130, 741, 621))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.spider_run = QtWidgets.QPushButton(self.centralwidget)
        self.spider_run.setGeometry(QtCore.QRect(820, 190, 161, 41))
        self.spider_run.setObjectName("spider_run")
        self.key_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.key_edit.setGeometry(QtCore.QRect(890, 100, 121, 21))
        self.key_edit.setObjectName("key_edit")
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(820, 100, 61, 21))
        self.key_label.setObjectName("key_label")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(820, 140, 54, 12))
        self.output_label.setObjectName("output_label")
        self.Network_spider = QtWidgets.QTextBrowser(self.centralwidget)
        self.Network_spider.setGeometry(QtCore.QRect(820, 30, 151, 41))
        self.Network_spider.setObjectName("Network_spider")
        self.output_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.output_edit.setGeometry(QtCore.QRect(890, 140, 121, 21))
        self.output_edit.setObjectName("output_edit")
        self.data_run = QtWidgets.QPushButton(self.centralwidget)
        self.data_run.setGeometry(QtCore.QRect(820, 290, 161, 41))
        self.data_run.setDefault(False)
        self.data_run.setObjectName("data_run")
        self.Data_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.Data_view.setGeometry(QtCore.QRect(830, 400, 151, 41))
        self.Data_view.setObjectName("Data_view")
        self.data_test = QtWidgets.QLabel(self.centralwidget)
        self.data_test.setGeometry(QtCore.QRect(820, 480, 54, 12))
        self.data_test.setObjectName("data_test")
        self.data_test_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.data_test_edit.setGeometry(QtCore.QRect(880, 480, 121, 21))
        self.data_test_edit.setObjectName("data_test_edit")
        self.data_test_2 = QtWidgets.QPushButton(self.centralwidget)
        self.data_test_2.setGeometry(QtCore.QRect(830, 510, 161, 41))
        self.data_test_2.setObjectName("data_test_2")
        self.data_output_2 = QtWidgets.QLabel(self.centralwidget)
        self.data_output_2.setGeometry(QtCore.QRect(820, 570, 54, 12))
        self.data_output_2.setObjectName("data_output_2")
        self.data_output = QtWidgets.QLineEdit(self.centralwidget)
        self.data_output.setGeometry(QtCore.QRect(880, 570, 121, 21))
        self.data_output.setObjectName("data_output")
        self.data_config = QtWidgets.QLabel(self.centralwidget)
        self.data_config.setGeometry(QtCore.QRect(820, 610, 54, 12))
        self.data_config.setObjectName("data_config")
        self.config_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.config_edit.setGeometry(QtCore.QRect(880, 610, 121, 21))
        self.config_edit.setObjectName("config_edit")
        self.data_build = QtWidgets.QPushButton(self.centralwidget)
        self.data_build.setGeometry(QtCore.QRect(830, 650, 161, 41))
        self.data_build.setObjectName("data_build")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 741, 101))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1116, 21))
        self.menubar.setObjectName("menubar")
        self.menudata_show = QtWidgets.QMenu(self.menubar)
        self.menudata_show.setObjectName("menudata_show")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menudata_show.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spider_run.setText(_translate("MainWindow", "运行"))
        self.key_label.setText(_translate("MainWindow", "关键字"))
        self.output_label.setText(_translate("MainWindow", "输出文件"))
        self.Network_spider.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">网络爬虫引擎</span></p></body></html>"))
        self.data_run.setText(_translate("MainWindow", "数据分析"))
        self.Data_view.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">数据可视化模块</span></p></body></html>"))
        self.data_test.setText(_translate("MainWindow", "输出文件"))
        self.data_test_2.setText(_translate("MainWindow", "测试"))
        self.data_output_2.setText(_translate("MainWindow", "输出文件"))
        self.data_config.setText(_translate("MainWindow", "配置文件"))
        self.data_build.setText(_translate("MainWindow", "建立"))
        self.menudata_show.setTitle(_translate("MainWindow", "data_show"))


class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str) #定义一个发送str的信号
    def write(self, text):
      self.textWritten.emit(str(text))


class WorkThread(QThread):
    trigger = pyqtSignal()
    def __init__(self):
        super(WorkThread,self).__init__()
    def run(self):
        self.file = self.output_edit.text()
        my_spider_init(self.file)
        my_spider_run(self.file)





class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.work = WorkThread()
        self.work.trigger.connect(self.my_display)

        self.spider_run.clicked.connect(self.spider_clicked)
        self.data_run.clicked.connect(self.data_clicked)
        # self.setWindowTitle('data_show')
        # self.setGeometry(5,30,1920,1080)


        self.webEngineView.load(QUrl("file:///index.html"))
        # self.setCentralWidget(self.browser)
        # self.setWindowIcon(QIcon('Logo.ico'))

    def outputWritten(self, text):
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textBrowser.setTextCursor(cursor)
        self.textBrowser.ensureCursorVisible()

    def spider_clicked(self):
        self.work.start()


    def data_clicked(self):
        data = pd.read_csv("company.csv")
        types = data['公司类型'].values
        addresses = data['地址'].values
        money_temp = data['资金'].values
        word_data = word_cut("info.txt")
        self.obj_graph = my_graph(bar_data(money_temp, types), map_data(addresses), pie_data(types), word_data)

    def my_display(self):
        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())

