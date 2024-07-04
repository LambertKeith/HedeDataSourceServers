from servers.preprocessing_server import DataPreprocessor


def test1():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\订单.xlsx',
        f'订单.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '订单'
    )
    file_preprocessor.preprocess()

def test2():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\男鞋商品信息数据.xls',
        f'男鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '男鞋商品信息数据'
    )
    file_preprocessor.preprocess()

def test3():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\男鞋物价信息查询数据.xls',
        f'男鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '男鞋物价信息查询数据'
    )
    file_preprocessor.preprocess()

def test4():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\女鞋商品信息数据.xls',
        f'女鞋商品信息数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '女鞋商品信息数据'
    )
    file_preprocessor.preprocess()

def test5():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\女鞋物价信息查询数据.xls',
        f'女鞋物价信息查询数据.xls',
        r'C:\Users\Admin\Desktop\process',
        '女鞋物价信息查询数据'
    )
    file_preprocessor.preprocess()

def test6():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\商品库存.xlsx',
        f'商品库存.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '商品库存'
    )
    file_preprocessor.preprocess()

def test7():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\月聚水潭.xlsx',
        f'月聚水潭.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '月聚水潭'
    )
    file_preprocessor.preprocess()

def test8():
    file_preprocessor = DataPreprocessor(
        r'C:\Users\Admin\Desktop\源表\月罗盘.xlsx',
        f'月罗盘.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '月罗盘'
    )
    file_preprocessor.preprocess()


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    # test5()   女鞋物价信息查询数据.xlsx
    test6()
    test7()
    test8()