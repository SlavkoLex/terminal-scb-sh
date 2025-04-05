import json

class JSONworker:

    __bufferJSON: list[dict] = []

    @classmethod
    def addDataInBuffer(cls, data: dict) -> None:
        JSONworker.__bufferJSON.append(data)

    @classmethod
    def addDataTopInBuffer(cls, listData: list[dict]) -> None:
        for data in listData[::-1]:
            JSONworker.__bufferJSON.insert(0, data)

    @classmethod
    def getDataBuffer(cls) -> list[dict]:
        return JSONworker.__bufferJSON
    
    @classmethod
    def clearBuffer(cls) -> None:
        JSONworker.__bufferJSON.clear()

    
    def __init__(self, JSONfile: str):
        self.__JSONfile: str = JSONfile

    def getJSONfile(self) -> str:
        return self.__JSONfile

    def writeJSONfile(self, dataArr: list[dict]) -> None:

        if(len(dataArr) < 1 or len(dataArr[0]) == 0):
            print(f'There is no data to save: {dataArr}')
        else:
            with open(self.__JSONfile, 'w', encoding='utf-8') as f:
                json.dump(dataArr, f, ensure_ascii=False, sort_keys=True, indent=1)

    def readeJSONfile(self) -> list[dict]:
            try:
                with open(self.__JSONfile, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except json.decoder.JSONDecodeError:
                pass


    def JSONfileInit(self):
        with open(self.__JSONfile, 'w'):
                pass


