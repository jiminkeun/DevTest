import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 창 설정
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

        # 로그인창 호출
        self.kiwoom.dynamicCall("commConnect()")

        # 텍스트 박스
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)
        
        # OnEventConnect 함수 발생시 event_connect 로 바인딩
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")

            self.text
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
# 이벤트 루프 진입
#app.exec_()