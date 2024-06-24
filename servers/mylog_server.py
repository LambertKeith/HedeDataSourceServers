# 日志模块
import logging
import inspect
from functools import wraps
import os



class CustomLogger:
    def __init__(self, name='CustomLogger', log_file=r'logs\app.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 设置调试级别
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 建立格式
        formatter = logging.Formatter('%(message)s')
        # Add formatter to ch
        ch.setFormatter(formatter)
        # Add ch to logger
        self.logger.addHandler(ch)

        # 日志文件初始化
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)


    def _log(self, level, message):      
        frame = inspect.currentframe().f_back.f_back
        filename = os.path.basename(frame.f_code.co_filename)
        lineno = frame.f_lineno
        log_message = f"[{logging.getLevelName(level)}]-[{self._current_time()}]-[{filename}]-[{lineno}]-[{message}]"
        self.logger.log(level, log_message)
        

    def debug(self, message):
        self._log(logging.DEBUG, message)
        

    def info(self, message):
        self._log(logging.INFO, message)
        

    def warning(self, message):
        self._log(logging.WARNING, message)
        

    def error(self, message):
        self._log(logging.ERROR, message)
        

    def critical(self, message):
        self._log(logging.CRITICAL, message)
        

    def _current_time(self):
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    def log_params_and_return(self, func):
        """打印入参出参的装饰器
        打印被装饰函数的入参出参

        Args:
            func (_type_): 被装饰函数
        """        
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            frame = inspect.currentframe().f_back
            filename = os.path.basename(frame.f_code.co_filename)
            lineno = frame.f_lineno
            params = inspect.signature(func).bind(*args, **kwargs).arguments
            self.info(f"{func_name} - 入参: {params}")
            result = func(*args, **kwargs)
            self.info(f"{func_name} - 出参: {result}")
            return result
        return wrapper



logger = CustomLogger()
'''
# example
from servers.mylog_server import logger

@logger.log_params_and_return
def example_function(a, b):
    logger.info("Executing example function")
    return a + b

example_function(5, 10)
'''