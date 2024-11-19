from typing import Final
from datetime import datetime
import string

name : string  = "bob" #variable name : type annotation
age : Final[int]  = 40 #Final makes consts (kind of)


 #return type annotation
def ShowDate() -> None:
    print(datetime.now())


class Handler:
    def __init__(self) -> None:
        self.time = datetime.now()

    def ShowDateTime(self) -> None:
        print(f'{self.time}')

    def __str__(self) -> str:
        return f'Right now we are: {self.time}'
        

mainHandler : Handler = Handler()
mainHandler.ShowDateTime()
print(mainHandler)