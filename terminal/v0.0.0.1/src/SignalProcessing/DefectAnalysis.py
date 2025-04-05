class DefectAnalysis:

    # Averages the value for each of the arrays (When the arrays with wheel data are > 1)
    @classmethod
    def getMiddle(cls, args: list[list[int]]) -> list[int]:

        resultList: list[int] = []
        iterator: int = 0 
        while (iterator <= len(args) -1):

            accumuletor: int = 0
            for i in args[iterator]:
                accumuletor += i

            resultList.append(accumuletor/len(args[iterator]))
            iterator+= 1  

        return resultList

    # Assessment of "Trends" (This feature allows you to determine the presence of a "Chipped" flaw on the composition wheel)
    @classmethod
    def trendAssessment(cls, middleRes: list[int]) -> list[int]:
        result: list[int] = [0 if middleRes[i]<middleRes[i+1] else 1 for i in range(len(middleRes)-1)]

        return result
    

    def __init__(self, signalArguments: list[list[int]]) -> None:
        self.__signalArguments = DefectAnalysis.trendAssessment(DefectAnalysis.getMiddle(signalArguments))

    # Analysis of prepared data for defects
    def defectDetection(self) -> int:

        counter: int = 0
        while(counter < len(self.__signalArguments)):
            if(self.__signalArguments[counter] == 1):
                break
            counter += 1

        result: int = 0

        for element in range(counter, len(self.__signalArguments)):
            if(self.__signalArguments[element] == 0):
                result = 1
                break

        return result
    

