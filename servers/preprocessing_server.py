# 文件下载和预处理
import os
# from .mylog_server import logger
import pandas as pd
import win32com.client as win32
import pythoncom

class DataPreprocessor:
    def __init__(self, file_path, file_name, out_put_folder, file_text):
        self.file_path = file_path
        self.file_name = file_name
        self.out_put_folder = out_put_folder
        self.output_file_name = f"{file_text}.xlsx"

    def preprocess(self):
        self.copy_convert_excel()
        head_row = self.findHead_row()
        self.delete_null_rows(head_row)

    def copy_convert_excel(self):
        file_ext = os.path.splitext(self.file_name)[1]
        print(file_ext)
        xls_file = self.file_path
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)

        pythoncom.CoInitialize()

        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(os.path.abspath(xls_file))
        # 如果excel存在，删除
        if os.path.exists(output_file_path):
            os.remove(output_file_path)
        # 保存新excel
        wb.SaveAs(os.path.abspath(output_file_path), FileFormat=51)
        wb.Close()
        excel.Application.Quit()
        
    def findHead_row(self):
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)
        print("output_file_path", output_file_path)
        df = pd.read_excel(output_file_path, header=None)
        num_rows = len(df)
        num_cols = len(df.columns)
        # print("here", df.head())
        for index in range(num_rows):
            # print(index)
            count = 0
            row = df.iloc[index]
            print(row)
            count = row.count()
            if count == num_cols:
                print(f"index:{index}")
                print(f"count:{count}")
                return index

    def delete_null_rows(self, head_row):
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)
        df = pd.read_excel(output_file_path, header=None)
        new_header = df.iloc[head_row]
        head_row = head_row + 1
        df = df[head_row:]
        df.columns = new_header
        df.to_excel(output_file_path, index=False)
        print(df.head())
