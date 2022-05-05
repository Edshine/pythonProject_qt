import sys
import MainWinSignalSlot
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    #创建一个QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个QMainWindow类的对象
    mainwindow = QMainWindow()
    #引用MainWinHorizontalLayout类并创建它的实例
    ui = MainWinSignalSlot.Ui_MainWindow()
    #创建该窗口的组件
    ui.setupUi(mainwindow)
    #展示该窗口
    mainwindow.show()
    #退出该程序
    sys.exit(app.exec_())