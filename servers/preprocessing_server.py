# 文件下载和预处理
import os
# from .mylog_server import logger
import pandas as pd
import win32com.client as win32
import xlrd
from openpyxl.utils.exceptions import InvalidFileException

class DataPreprocessor:
    def __init__(self, file_path, file_name, out_put_folder, file_text):
        self.file_path = file_path
        self.file_name = file_name
        self.out_put_folder = out_put_folder
        self.output_file_name = f"{file_text}.xlsx"

    def preprocess(self):
        self.copy_convert_excel()
        file_ext = os.path.splitext(self.file_name)[1]
        if file_ext == '.xls':
            head_row = self.findHead_row()
            self.delete_null_rows(head_row)

    def copy_convert_excel(self):
        file_ext = os.path.splitext(self.file_name)[1]
        print(file_ext)
        xls_file = self.file_path
        # self.df = pd.read_excel(xls_file, sheet_name=None)  # 读取所有的 sheet
        # # 构建输出文件的完整路径
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)
        # # 将数据写入 .xlsx 文件
        # with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        #     for sheet_name, sheet_df in self.df.items():
        #         sheet_df.to_excel(writer, sheet_name='sheet1', index=False)
        # print(f'{xls_file} 转换为 {output_file_path} 完成。')
        # print(f"处理后的文件保存到：{output_file_path}")
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(os.path.abspath(xls_file))
        wb.SaveAs(os.path.abspath(output_file_path), FileFormat=51)
        wb.Close()
        excel.Application.Quit()
        
    def findHead_row(self):
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)
        print("output_file_path", output_file_path)
        df = pd.read_excel(output_file_path)
        print("here", df.head())
        count = 0
        for index, row in df.iterrows():
            print(index)
            for item in row:
                if pd.isnull(item) or item == '':
                    pass
                    # print(f'项 "{item}" 是空的')
                else:
                    count += 1
                    if count == len(row):
                        print(count)
                        print(index)
                        return index

    def delete_null_rows(self, head_row):
        output_file_path = os.path.join(self.out_put_folder, self.output_file_name)
        df = pd.read_excel(output_file_path)
        new_header = df.iloc[head_row]
        head_row = head_row + 1
        df = df[head_row:]
        df.columns = new_header
        df.to_excel(output_file_path, index=False)
        print(df.head())
