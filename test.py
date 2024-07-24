from servers.preprocessing_server import DataPreprocessor

if __name__ == '__main__':
    file_preprocessor = DataPreprocessor(
        r'\\Creation\超级共享\影刀技术开发部共享\管家婆数据导出\2024-07-29\男鞋商品信息.xlsx',
        f'男鞋商品信息.xlsx',
        r'C:\Users\Admin\Desktop\process',
        '男鞋商品信息'
    )
    file_preprocessor.preprocess()
