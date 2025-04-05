from datetime import datetime
import re

class DateTimeForSCBSh:

    # Gets the current date and time of the system in which the "Terminal SCB-Sh" program is running. 
    # It is used to set the received time value on the device "SCB-Sh".
    @classmethod
    def __initDateTime(cls) -> list[int]:
        dateTime: list[int] = re.split(r'[- :.]+',str(datetime.now()))
        border: int = len(dateTime)-1

        return [int(i) for i in dateTime[:border]]

    def __init__(self):
        self.__time = DateTimeForSCBSh.__initDateTime()

    def getDateTime(self) -> list[int]:
        return self.__time

    def setTime(self, newTime: list[int]):
        self.__time = newTime

