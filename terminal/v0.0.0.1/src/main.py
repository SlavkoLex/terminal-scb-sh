from Termnal.StartTerminal import startTerminal
import sys
from pathlib import Path
import os

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

def main():

    # Create Error-Log catalog
    errDir = f'{os.path.expanduser("~")}/ErrLog' 
    errFile = f'{errDir}/ErrLogJSON.json'

    if Path(errDir).exists() and Path(errDir).is_dir():
        if Path(errFile).is_file() == False:
            with open(errFile, 'w'):
                print("\n An ModbusRTU error log file has been created (PATH: ~/ErrLog/ErrLogJSON.json)\n[ Фалй логирования ошибок ModbusRTU успешно создан (ПУТЬ: ~/ErrLog/ErrLogJSON.json) ]\n")
        else:
            print("\n ModbusRTU Error log file exist (PATH: ~/ErrLog/ErrLogJSON.json)\n[ Файл логирования ошибок ModbusRTU ранее был создан (ПУТЬ: ~/ErrLog/ErrLogJSON.json) ]\n")
    else:
        os.mkdir(errDir)
        with open(errFile, 'w'):
            print("\n The ErrLog directory and ErrLogJSON.json file were successfully created (PATH: ~/ErrLog/ErrLogJSON.json)\n[ Каталог ErrLog с файлом ErrLogJSON.json были успешно созданы (ПУТЬ: ~/ErrLog/ErrLogJSON.json)]\n")

    # Create Data-Log catalog
    pathToDataDir = f'{os.path.expanduser("~")}/DataLog'

    if not Path(pathToDataDir).exists() and not Path(pathToDataDir).is_dir():
        print(f'\nThe data log storage "{pathToDataDir}" directory has been created successfully!\n[Каталог хранения лога данных "{pathToDataDir}" создан успешно!]')
        os.mkdir(pathToDataDir)
    else:
        print(f'\nThe data log directory "{pathToDataDir}" was previously created!\n[Каталог лога данных "{pathToDataDir}" ранее был создан!]')

    startTerminal(TrainInfoLocal, TerminalDialogLocal, Months, GenericPhrases, Defect, ExceptionMessage, pathToDataDir)
    


if __name__ == "__main__":
    main()
