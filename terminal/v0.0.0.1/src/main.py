from Termnal.StartTerminal import startTerminal
import sys

__LOCAL_KEY:str = ""
__LOCAL_INDEX: int = 1

if(len(sys.argv) > __LOCAL_INDEX):
    __LOCAL_KEY = sys.argv[__LOCAL_INDEX]


if(__LOCAL_KEY == "R"):
    from localization.ru.RuTrainInformation import TrainInfoLocal
    from localization.ru.RuTerminalDialog import TerminalDialogLocal
    from localization.ru.RuMonths import Months
    from localization.ru.RuGenericPhrases import GenericPhrases
    from localization.ru.RuExceptions import ExceptionMessage
    from localization.ru.RuDefect import Defect

elif(__LOCAL_KEY == "E"):
    from localization.en.EnTrainInformation import TrainInfoLocal
    from localization.en.EnTerminalDialog import TerminalDialogLocal
    from localization.en.EnMonths import Months
    from localization.en.EnGenericPhrases import GenericPhrases
    from localization.en.EnExceptions import ExceptionMessage
    from localization.en.EnDefect import Defect

else:
    from localization.en.EnTrainInformation import TrainInfoLocal
    from localization.en.EnTerminalDialog import TerminalDialogLocal
    from localization.en.EnMonths import Months
    from localization.en.EnGenericPhrases import GenericPhrases
    from localization.en.EnExceptions import ExceptionMessage
    from localization.en.EnDefect import Defect

    print("\n!!You did not select the language for the Terminal SCB-Sh v0.0.0.1 program, English was set by default!!\n")

def main(TrainInfoLocal: dict, TerminalDialogLocal: dict, Months: dict, GenericPhrases: dict, Defect: dict,  ExceptionMessage: dict):
    startTerminal(TrainInfoLocal, TerminalDialogLocal, Months, GenericPhrases, Defect, ExceptionMessage)


if __name__ == "__main__":
    main(TrainInfoLocal, TerminalDialogLocal, Months, GenericPhrases, Defect, ExceptionMessage)
