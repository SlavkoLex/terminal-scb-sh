import json
import os

class JsonErrorLogWorker: 

    def __init__(self):

        self.__errFileName = f'{os.path.expanduser("~")}/ErrLog/ErrLogJSON.json' # Проверяется с запуском программы
        self.__errrBuffer: list[dict] = []

    def writeErrBuffer(self, date: str, message: str, error: str):
        self.__errrBuffer.append({'date': date, 'message': message, 'error':error})

    def clearErrBuffer(self):
         self.__errrBuffer.clear()

    def getErrBuffer(self):
        return self.__errrBuffer
    
    def getFileName(self):
        return self.__errFileName
    
    def wtireErrLogJson(self):
        with open(self.__errFileName, 'w', encoding='utf-8') as f:
            json.dump(self.__errrBuffer, f, ensure_ascii=False, sort_keys=True, indent=1)

    def readeJSONfile(self) -> list[dict]:
            try:
                with open(self.__errFileName, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.decoder.JSONDecodeError:
                pass
