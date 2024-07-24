from fastapi import FastAPI, HTTPException, Depends, Request, Response, Form, UploadFile, File
from pydantic import BaseModel, ValidationError
import os
from utils.returns_format import ServerState
from servers.preprocessing_server import DataPreprocessor
from servers.db_write_server import TableInserter


server_state = ServerState()
app = FastAPI()



# Define a data model
class Item(BaseModel):
    file_path: str
    table_name: str


# Define a GET endpoint
@app.get("/")
def get_data_source():
    return {"message": "Hello,World!"}


# Define a POST endpoint
@app.post("/data_source/")
def create_item(item: Item):
    try:
        test(item.file_path, item.table_name)
        # return Item(**item.dict())
        return server_state.return_success_info("success")

    except Exception as e:
        import traceback
        traceback.print_exc()
        return server_state.return_fail_info("fail!", 500)
    

def test(file_path, table_name):
    print("调用了test方法")
    print("文件路径："+file_path)
    file_name = os.path.basename(file_path)
    file_txt = os.path.splitext(file_name)[0]
    output_file_name = f"{file_txt}.xlsx"
    out_put_folder = r'C:\Users\Admin\Desktop\process'
    output_file_path = os.path.join(out_put_folder, output_file_name)

    file_preprocessor = DataPreprocessor(
        file_path, file_name, out_put_folder, file_txt)
    file_preprocessor.preprocess()
    print("预处理完成")

    table_inserter = TableInserter(
        output_file_path,
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        table_name
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()
    print("插入数据库成功")
