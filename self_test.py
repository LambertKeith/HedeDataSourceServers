from servers.preprocessing_server import DataPreprocessor
from servers.db_write_server import TableInserter


def test1():
    file_preprocessor = DataPreprocessor(
        r'\\Creation\超级共享\影刀技术开发部共享\聚水潭\千百度\07.29\商品库存.xlsx',
        f'商品库存.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '商品库存'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\process\商品库存.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'test'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()



if __name__ == "__main__":
    test1()
