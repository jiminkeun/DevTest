import win32com.client

# 익스플로러 객체 바인딩
#explorer = win32com.client.Dispatch("InternetExplorer.Application")
#explorer.Visible = True

# 워드 객체 바인딩
#word = win32com.client.Dispatch("Word.Application")
#word.Visible = True

# 엑셀 객체 바인딩
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
# 워크북 객체 생성
#wb = excel.Workbooks.Add()
# 워크시트 객체 생성
#ws = wb.Worksheets("Sheet1")
# 엑셀 쓰기(파일 저장)
#ws.Cells(1,1).Value = "hello world"
#wb.SaveAs("E:\\Dev\\PYTHON_WORKSTATION\\pythonTest\\newTest.xlsx")
#excel.Quit()

# 엑셀 읽기
wb = excel.Workbooks.Open("E:\\Dev\\PYTHON_WORKSTATION\\pythonTest\\readTest.xlsx")
ws = wb.ActiveSheet
#print(ws.Cells(1,1).Value)
# 컬러입히기
ws.Cells(5,1).Value = "LG화학"
ws.Range("B5").Value = "15000"
ws.Range("B1:B5").Interior.ColorIndex = 10
#wb.SaveAs("E:\\Dev\\PYTHON_WORKSTATION\\pythonTest\\readTest.xlsx")
#excel.Quit()