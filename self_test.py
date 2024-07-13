from servers.preprocessing_server import DataPreprocessor
from servers.db_write_server import TableInserter
import win32com
from main import Item
import os


def test1():
    file_preprocessor = DataPreprocessor(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\男鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\源表\男鞋商品信息数据.xls',
        f'男鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '男鞋商品信息数据'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\男鞋商品信息数据.xlsx',
        r'C:\Users\Admin\Desktop\process\男鞋商品信息数据.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'man_shoes_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test2():
    file_preprocessor = DataPreprocessor(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\男鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\源表\男鞋物价信息查询数据.xls',
        f'男鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '男鞋物价信息查询数据'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\男鞋物价信息查询数据.xlsx',
        r'C:\Users\Admin\Desktop\process\男鞋物价信息查询数据.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'man_price_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test3():
    file_preprocessor = DataPreprocessor(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\女鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\源表\女鞋商品信息数据.xls',
        f'女鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '女鞋商品信息数据'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\女鞋商品信息数据.xlsx',
        r'C:\Users\Admin\Desktop\process\女鞋商品信息数据.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'woman_shoes_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test4():
    file_preprocessor = DataPreprocessor(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\女鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\源表\女鞋物价信息查询数据.xls',
        f'女鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '女鞋物价信息查询数据'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        # r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-19\女鞋物价信息查询数据.xlsx',
        r'C:\Users\Admin\Desktop\process\女鞋物价信息查询数据.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'women_price_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test5():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\订单.xlsx',
        f'订单.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '订单'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\process\订单.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'orders_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test6():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\商品库存.xlsx',
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
        'product_stock_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test7():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\月聚水潭.xlsx',
        f'月聚水潭.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '月聚水潭'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\process\月聚水潭.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'month_gatherwater_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


def test8():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\月罗盘.xlsx',
        f'月罗盘.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '月罗盘'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\process\月罗盘.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'lunar_compass_db'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()

def test9():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\采购单管理.xlsx',
        f'采购单管理.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '采购单管理'
    )
    file_preprocessor.preprocess()

    table_inserter = TableInserter(
        r'C:\Users\Admin\Desktop\process\采购单管理.xlsx',
        'root',
        '111111',
        '192.168.10.207',
        '3306',
        'yuting_study',
        'purchase_orders'
    )
    table_inserter.read_excel_to_df()
    table_inserter.insert_data_to_mysql()


# item = Item()


if __name__ == "__main__":

    # test1()
    # test2()
    # test3()
    # test4()
    # test9()

    item = Item()
    # item.file_path = '1'
    # item.table_name = '2'
    # print(item)
    # print(item.file_path, item.table_name)
    # file_name = os.path.basename(Item.file_path)
    # file_txt = os.path.splitext(file_name)[0]
    # file_preprocessor = DataPreprocessor(
    #     Item.file_path, file_name, r'C:\Users\Admin\Desktop\ process', file_txt)
    # file_preprocessor.preprocess()
    #
    # table_inserter = TableInserter(
    #     Item.file_path,
    #     'root',
    #     '111111',
    #     '192.168.10.207',
    #     '3306',
    #     'yuting_study',
    #     Item.table_name
    # )
    # table_inserter.read_excel_to_df()
    # table_inserter.insert_data_to_mysql()
