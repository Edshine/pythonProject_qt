import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
# 添加图标
from PyQt5.QtGui import QIcon
#创建一个类，从QMainWindow继承
class FirstMainWin(QMainWindow):
    #parent指代实体的窗口对象，也就是主函数里面的那个mainWindow = QMainWindow()
    #parent=None表示该窗口为顶级窗口
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        #设置窗口的尺寸
        self.resize(400,300)

        #获得状态栏
        self.status = self.statusBar()

        self.status.showMessage('只存在5s的消息',5000)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    #图标
    app.setWindowIcon(QIcon('D:/桌面/picture/youself_1.jpg'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())

