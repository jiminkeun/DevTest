import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# sys.argv : 현재 소스코드의 절대경로
#app = QApplication(sys.argv)
# 화면 구성(UI)
#label = QLabel("Hello PyQt")
#label2 = QPushButton("Quit")
# 화면 노출
#label.show()
#label2.show()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 창 설정
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        # 로긴 버튼 생성
        btnLogin = QPushButton("Login", self)
        btnLogin.move(20, 20)
        btnLogin.clicked.connect(self.btnLogin_clicked)

        # Check State 버튼 생성
        btnChkState = QPushButton("Check State", self)
        btnChkState.move(20, 50)
        btnChkState.clicked.connect(self.btnChkState_clicked)

    # 버튼 클릭 이벤트
    def btnLogin_clicked(self):
        #QMessageBox.about(self, "login", "clicked")
        ret = self.kiwoom.dynamicCall("CommConnect()")

    def btnChkState_clicked(self):
        #QMessageBox.about(self, "state", "clicked")
        if self.kiwoom.dynamicCall("GetConnectState()") == 0:
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
# 이벤트 루프 진입
#app.exec_()