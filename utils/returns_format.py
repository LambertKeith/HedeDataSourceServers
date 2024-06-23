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

        """Return information package

        Args:
            response (Response): Request

        Returns:
            ServerInfo: Information object
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
        """Return information package

        Args:
            response (Response): Request

        Returns:
            ServerInfo: Information object
        """
        return ServerInfo(
            start_time=self.start_time,
            status_code=status_code,
            headers={}, # Uncomment if needed
            details={
                "message": info
            }
        )