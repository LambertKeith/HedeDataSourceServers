from fastapi import Response
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any
import pytz

class ServerInfo(BaseModel):
    start_time: datetime
    status_code: int
    headers: Dict[str, Any]
    details: Dict[str, Any]

class ServerState:
    def __init__(self):
        self.start_time = datetime.now(pytz.utc)
        self.request_count = 0

    def return_success_info(self, info: str = "Server is running smoothly") -> ServerInfo:
        """成功消息

        Args:
            info (str, optional): _description_. Defaults to "Server is running smoothly".

        Returns:
            ServerInfo: _description_
        """        
        return ServerInfo(
            start_time=self.start_time,
            status_code=200,
            headers={}, # Uncomment if needed
            details={
                "message": info
            }
        )


    def return_fail_info(self, info: str = "Server is running smoothly", status_code: int=500) -> ServerInfo:
        """失败消息

        Args:
            info (str, optional): 信息. Defaults to "Server is running smoothly".
            status_code (int, optional): 状态码. Defaults to 500.

        Returns:
            ServerInfo: _description_
        """        
        return ServerInfo(
            start_time=self.start_time,
            status_code=status_code,
            headers={}, # Uncomment if needed
            details={
                "message": info
            }
        )