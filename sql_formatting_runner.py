import sys
import locale
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from original import *
import os
import sys
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLabel, QLineEdit, QToolButton, QMessageBox, QDialog,QFrame

from PyQt5.QtGui import QFontDatabase

form_class = uic.loadUiType("sql_formatter.ui")[0]

# 로케일 설정
locale.setlocale(locale.LC_ALL, '')

class BotWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Moon SQL Formatter")
        
        # 예시로 창의 크기나 다른 설정을 추가할 수 있습니다.
        self.setGeometry(300, 100, 1264, 882)  # 창의 크기 설정 (x, y, width, height)
        self.setContentsMargins(0, 0, 0, 0)  # top, left, bottom, right


        # 예시로 텍스트 에디터를 설정하는 코드 (UI 파일에서 가져온 widget에 따라 수정 필요)
        self.text_edit = self.findChild(QTextEdit, 'textEdit')  # UI에서 'text_edit'라는 이름의 위젯을 찾습니다.
        self.text_edit2 = self.findChild(QTextEdit, 'textEdit_2')  # UI에서 'text_edit'라는 이름의 위젯을 찾습니다.
        self.pushButton = self.findChild(QPushButton, 'input_box')  # 버튼
        self.pushButton2 = self.findChild(QPushButton, 'del_box')  # 버튼

        self.main_title = self.findChild(QLabel, 'main_title')  # TITLE
        self.input_title = self.findChild(QLabel, 'input_title')  # TITLE
        self.output_title = self.findChild(QLabel, 'output_title')  # TITLE

        #글자수 체크
        self.input_cnt = self.findChild(QLineEdit, 'input_cnt')  
        self.output_cnt = self.findChild(QLineEdit, 'output_cnt')  

        self.note_button = self.findChild(QToolButton, 'note')  # UI에서 'note' 버튼을 찾습니다.

        self.title_beta = self.findChild(QLabel,'label_4')
        self.title_moon = self.findChild(QLabel ,'label_11')



        # 버튼 클릭 시 SQL 정렬 실행
        self.pushButton.clicked.connect(self.on_button_click)

    
        self.text_edit.setPlaceholderText("정렬할 SQL쿼리를 입력해주세요.") 
        self.text_edit2.setPlaceholderText("정렬된 SQL쿼리가 출력됩니다.") 

        #마우스 커서 바꿈
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.pushButton2.setCursor(Qt.PointingHandCursor)
        self.note_button.setCursor(Qt.PointingHandCursor)

        # 'textEdit_2' 읽기 전용
        self.text_edit2.setReadOnly(True)
        self.input_cnt.setReadOnly(True)
        self.output_cnt.setReadOnly(True)

        self.is_formatted = False  # 포맷이 완료되었는지 여부를 추적하는 변수

        self.title_beta.setStyleSheet("""
            QLabel {
                
                color: red;                            /* 텍스트 색상: 빨간색 */
                font: bold 12pt "Microsoft Yi Baiti";          /* 둥글둥글한 글씨체 + 굵게 + 10pt */
                background-color: transparent;              /* 배경 없음 */
                padding-left: 15px;

            }
        """)
        self.title_moon.setStyleSheet("""
            QLabel {            
                color: rgb(255, 255, 255);                           
                font: 57 24pt "Noto Sans KR Medium";
                background-color: transparent;              /* 배경 없음 */


            }
        """)        

        #마우스 호버시 색 변경 
        self.pushButton.setStyleSheet("""
            QPushButton {
                border-radius: 15px;                      /* 둥근 모서리 */
                border: 1px solid #4048e1;                /* 테두리 색상 (파란색) */
                background-color: rgb(46, 140, 255);
                color: rgb(255, 255, 255);                /* 텍스트 색상 (흰색) */
                font-size: 15px;                          /* 폰트 크기 */
             }
            QPushButton:hover {
                background-color: rgb(36, 110, 210);   /* 진한 파란색 */
            }
            QPushButton:pressed {
                background-color: rgb(26, 90, 170);       /* 눌렀을 때 가장 진한 파란색 */
            }
        """)
        self.pushButton2.setStyleSheet("""
            QPushButton {
                border-radius: 15px;                      /* 둥근 모서리 */
                border: 1px solid #4048e1;                /* 테두리 색상 (파란색) */
                background-color: rgb(253, 253, 253);
                color: rgb(0, 0, 0);                /* 텍스트 색상 (흰색) */
                font-size: 15px;                          /* 폰트 크기 */
            }

            QPushButton:hover {
                background-color: rgb(230, 230, 230);   /* 살짝 진해진 회색 */
            }

            QPushButton:pressed {
                background-color: rgb(210, 210, 210);   /* 누를 때 더 진한 색 */
            }
        """)


        ###테두리 변경
        self.text_edit.setStyleSheet("""
            QTextEdit {
                border: 2px solid #5A6BFF ;                /* 테두리 색상 (초록색) */
                border-radius: 10px;                       /* 둥근 모서리 */
                background-color: white;                   /* 배경색 (흰색) */
                padding: 5px;                             /* 안쪽 여백 */
                font: 25 10pt "Microsoft YaHei Light";
            }
        """)

        self.text_edit2.setStyleSheet("""
            QTextEdit {
                border: 2px solid rgb(60, 65, 180) ;                /* 테두리 색상 (초록색) */
                border-radius: 10px;                       /* 둥근 모서리 */
                background-color: white;                   /* 배경색 (흰색) */
                padding: 5px;                             /* 안쪽 여백 */
                font: 25 10pt "Microsoft YaHei Light";
            }
        """)

        #input박스 타이틀
        self.input_title.setStyleSheet("""
                QLabel {
                color: rgb(185, 200, 250);                 /* 부드러운 연보라-블루 톤 */
                font: bold 12pt "Segoe UI";                /* 깔끔한 볼드체 */
                padding: 1px 2px;                         /* 여백 */
                background-color: rgba(255, 255, 255, 0);  /* 투명 배경 */
            }
        """)
        #output박스 타이틀
        self.output_title.setStyleSheet("""
                QLabel {
                    color: rgb(130, 140, 255);                   /* 살짝 밝은 블루 → 결과 강조 */
                    font: bold 12pt "Segoe UI";                  /* 같은 폰트로 통일 */
                    padding: 1px 2px;                   /* 위 여백 */            
                    background-color: transparent;
                }
        """)

        self.main_title.setStyleSheet("""
            QLabel {
                font: 22pt "Century Gothic";            /* 폰트 스타일과 크기 */
                color: rgba(51, 51, 51, 1);              /* 밝은 파란색 텍스트 */
                font-weight: bold;                     /* 텍스트 굵기 강조 */
                text-align: center;                    /* 텍스트 중앙 정렬 */
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);  /* 텍스트 그림자 효과 */
            }
        """)      
        
        #마진 삭제
        self.setContentsMargins(0, 0, 0, 0)  # top, left, bottom, right

        # 글자 수 실시간 업데이트 연결
        self.text_edit.textChanged.connect(self.update_char_count)

        
        # text_edit2는 버튼 클릭 시 글자 수 업데이트
        self.pushButton2.clicked.connect(self.on_clear_button_click)


        # 툴바 버튼 추가 (패치노트)
        self.note_button.clicked.connect(self.show_patch_note) 
        self.note_button.setText("공지")


        # 버튼 스타일 설정
        self.note_button.setStyleSheet("""
            QToolButton {
                background-color: rgb(255, 165, 0);        /* 버튼 배경 색상 (오렌지색) */
                border: 2px solid rgb(255, 140, 0);        /* 버튼 테두리 색상 */
                border-radius: 10px;                       /* 둥근 모서리 */
                color: white;                              /* 글자 색상 (흰색) */
                font: bold 10pt "Segoe UI";                 /* 글꼴 크기 및 스타일 */
            }
            QToolButton:hover {
                background-color: rgb(255, 140, 0);        /* 마우스 hover 상태에서 배경 색상 (더 진한 오렌지) */
            }
            QToolButton:pressed {
                background-color: rgb(255, 120, 0);        /* 클릭 상태에서 배경 색상 (어두운 오렌지) */
            }
        """)

    def show_patch_note(self):
        # 패치 노트 내용
        patch_note = """
        1. JOIN 구문 앞에 LEFT, RIGHT 등 안 붙이면 정렬 제외
        2. 서브쿼리 안의 UNION 정렬 제외
        3. CTE 구문, 되도록 주석은 ()안에 사용 권장
        4. SELECT 첫 컬럼이 CASE 문은 정렬 제외      


        2025.04.29(패치노트) 
        - 내장 함수 안에 FROM 있는경우 예외 처리(완료)
        - 맨처음이 /**/으로 시작하는 부분 예외 처리(완료) 
        - /**/안에 나오는 AND OR 예외처리 -> 애를 그냥 /**/안에 내용을 치환 후 마지막에 롤백하는걸로 함수 만들 예정(완료)
        - [ ] 사이의 내용 치환(정렬시 부분 정렬 깨짐짐) -> 완료 

        """
        # 팝업창을 띄우는 부분
        dialog = QDialog(self)
        dialog.setWindowTitle("공지사항")  # 창 제목 설정
        dialog.setFixedSize(800, 400)  # 창 크기 설정 (너비 600, 높이 400)

        # QTextEdit 위젯을 생성하고 내용을 넣습니다.
        text_edit = QTextEdit(dialog)
        text_edit.setText(patch_note)
        text_edit.setAlignment(Qt.AlignLeft)  # 내용 왼쪽 정렬
        text_edit.setReadOnly(True)  # 읽기 전용으로 설정
        text_edit.setGeometry(10, 20, 760, 360)  # 텍스트 영역 위치 및 크기 설정

        font = text_edit.font()
        font.setPointSize(10)  # 글자 크기 설정 (12포인트로 설정)
        text_edit.setFont(font)

        # Dialog 표시
        dialog.exec_()
        


    #버튼 클릭 이벤트: 
    def on_button_click(self):
        # 이미 정렬이 완료된 경우
        if self.is_formatted:
            QMessageBox.information(self, "정보", "이미 정렬이 완료되었습니다.")
            self.is_formatted =False
            return

        sql_query = self.text_edit.toPlainText().strip()

        # 먼저: 입력창이 비워있다면
        if not sql_query:
            QMessageBox.warning(self, "입력 오류", "쿼리를 입력해주세요.")
            return

        # 다음: SELECT, FROM 키워드가 없으면
        if not ('select' in sql_query.lower() and 'from' in sql_query.lower()):
            QMessageBox.warning(self, "형식 오류", "쿼리 형식이 맞지 않습니다.")
            self.text_edit.clear()  # 입력창 비움
            # 정렬 초기화
            self.is_formatted = False
            return
        
        #괄호의 짝 맞는지 확인하는 함수.
        try:
            sql_query = self.validate_parentheses(sql_query)
        except ValueError as e:
            QMessageBox.critical(self, "SQL 구문 오류", str(e))
            self.text_edit.clear()  # 입력창 비우기
            # 정렬 초기화
            self.is_formatted = False
            return


        # exec_sql_formatting 함수 호출, SQL 쿼리를 인자로 전달
        self.exec_sql_formatting(sql_query)

        # 정렬 완료 처리
        self.is_formatted = True  # 포맷 완료
        
        # 버튼 클릭 후 text_edit2의 글자 수 업데이트
        self.update_char_count_output()

    #버튼 클릭시 output상자로 내용 업데이트
    def exec_sql_formatting(self,sql_query):

        
        try:
            final_sql = last_start(sql_query)

        except Exception as e:
            # 경고창 띄우기
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)  # 경고 아이콘 설정
            msg.setWindowTitle("에러")  # 창 제목 설정
            msg.setText(str(e))  # 메시지 텍스트 설정
            msg.setStandardButtons(QMessageBox.Ok)  # '확인' 버튼만 추가
            msg.exec_()  # 경고창 실행

            self.text_edit.clear()
            self.text_edit2.clear()

            # 포맷 상태를 False로 변경
            self.is_formatted = False

            return
        
        # 예외가 발생하지 않으면 정상적으로 포맷된 SQL을 출력창에 추가
        self.textEdit_2.append(final_sql)
        

    #삭제 버튼 처리
    def on_clear_button_click(self):
        reply = QMessageBox.question(
            self,
            "쿼리 삭제 확인",
            "정렬된 쿼리를 삭제합니다.\n계속하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            #self.text_edit.clear()
            self.text_edit2.clear()

            # 정렬 완료 초기화
            self.is_formatted = False  
    #괄호 쌍 맞는지 체크
    def validate_parentheses(self, sql: str):  # self 추가
        open_count = sql.count('(')
        close_count = sql.count(')')

        if open_count != close_count:
            raise ValueError(f"괄호 수가 맞지 않습니다! 여는 괄호: {open_count}, 닫는 괄호: {close_count}")
        return sql

        

    # 글자 수 업데이트 함수
    def update_char_count(self):

        #실제 작성된 글자수 카운팅
        input_len = len( re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', self.text_edit.toPlainText()))
       # output_len = len( re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', self.text_edit.toPlainText()))
        self.input_cnt.setText(f"글자 수 : {input_len}")
        #self.output_cnt.setText(f"글자 수 : {output_len}")

        #self.output_cnt.setText(f"{output_len}자")
    def update_char_count_output(self):
        # text_edit2에 대한 글자 수 카운팅
        output_len = len(re.findall(r'[A-Za-z0-9\(\),\.\'\*=-]', self.text_edit2.toPlainText()))
        self.output_cnt.setText(f"글자 수 : {output_len}")
        
    def resource_path(relative_path):
        """PyInstaller 실행 시에도 리소스 경로를 찾기 위한 함수"""
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

# QApplication 객체 생성 (PyQt5 애플리케이션을 실행하기 위한 필수 코드)
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)  # PyQt5 애플리케이션 객체 생성
        window = BotWindow()  # BotWindow 객체 생성
        window.show()  # UI 창 표시
        sys.exit(app.exec_())  # 이벤트 루프 시작
        #uic.loadUi(resource_path("sql_formatter.ui"), self)
    except Exception as e:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(traceback.format_exc())
        print(f"에러 발생: {e}")
    input("\n[Enter] 키를 누르면 창이 닫힙니다...")


