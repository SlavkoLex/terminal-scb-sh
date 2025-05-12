from PollModbusRTU.PollSCBSh import PollMbsSlave
from Termnal.TerminalInit import terminalInit
from DataSave.JSONworkerForData import JSONworker
from AdjustSCBSh.DateTimeForSCBSh import DateTimeForSCBSh
from NetConnection.CheckNetConnect import checkNetConnect
from ErrrorDeviceLog.JSONErrorLogWorker import JsonErrorLogWorker

# Determining the wheel defect
from SignalProcessing.DefectAnalysis import DefectAnalysis
from SignalProcessing.ParasiticVibrationFilter import parasiticConversionChecker

import configparser
from pathlib import Path
from termcolor import colored
from datetime import datetime
import os.path


def startTerminal(trainInfoLocal: dict, terminalLocal: dict, months: dict, genPhrases: dict, defectInfo: dict, exMess: dict):

# Create Mbs Error Logger object

    errorMbsWarkerLogger: JsonErrorLogWorker = JsonErrorLogWorker()

# Connect to SCB-Sh

    print(colored(f"\n<< {genPhrases["Greeting"]} >>\n", 'white', attrs=["bold"])) # Greeting

    confFile: str = "ModbusRTUportConf.ini"

    if not (os.path.exists(confFile)):
        print(colored(f"\n!!! {genPhrases["NoConfFile"]} '{confFile}'!!!\n", "red", attrs=["bold"]))
        raise SystemExit(1)
    
    infoMbsDevice: dict = terminalInit(terminalLocal)

    confsMbs = configparser.ConfigParser()

    confsMbs.read(confFile)

    try:
        mbsSlave = PollMbsSlave(
            infoMbsDevice["portPath"], 
            int(infoMbsDevice["addressSlave"]), 
            int(confsMbs["PortConfig"]["BAUDRATE"]), 
            int(confsMbs["PortConfig"]["COUNT_BITS"]), 
            confsMbs["PortConfig"]["PARITY_BIT"], 
            int(confsMbs["PortConfig"]["STOP_BIT"]),
            float(confsMbs["PortConfig"]["TIMEOUT"])
        )
    except Exception:
        print(colored(f"\n!!! {exMess["PortAdrrErr"]} !!!\n", "red", attrs=["bold"]))
        raise SystemExit(1)
    

# Auto time correction for "SCB-Sh device"
    print(colored(f"\n{genPhrases["TimeAdjust"]}\n", "white", attrs=["bold"]))

    newDateTime: list[int]  =  DateTimeForSCBSh().getDateTime()

    try:
        mbsSlave.adjustTime(newDateTime)
    except Exception:

        print(colored(f"\n!!! {exMess["CommunicationErr"]} !!!\n", "red", attrs=["bold"]))

        # Record information in an ErrLogJSON.json file
        if errorMbsWarkerLogger.readeJSONfile() == None:
            errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while adjusting time")
            errorMbsWarkerLogger.wtireErrLogJson() 
            errorMbsWarkerLogger.clearErrBuffer()
        else:
            for mapObj in errorMbsWarkerLogger.readeJSONfile(): 
                errorMbsWarkerLogger.writeErrBuffer(mapObj['date'], mapObj['message'], mapObj['error'])

            errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while adjusting time")
            errorMbsWarkerLogger.wtireErrLogJson() 
            errorMbsWarkerLogger.clearErrBuffer() 

        # Exception handle: Polling the device until it responds
        mbsSlave.noComminicationHandler()

        # If the device responds, repeat the operation that resulted in the error to 
        # ensure further correct operation of the program.
        mbsSlave.adjustTime(newDateTime)

# Checking the Internet connection
    if not (checkNetConnect()):
       print(colored(f"\n{genPhrases["NetConnectStatus"]}\n", 'white', attrs=["bold"]))

# The logic of polling and information output

    print(colored(f"\n************ {genPhrases["LineListening"]} '{infoMbsDevice["sensorPoint"]}' ************\n", 'white', attrs=["bold"])) # LOCAL RU EN

    dataSCBbuffer: list = [] # Buffer used to filter out duplicated data

# The name of the JSON Log file where all the information will be saved
    JSONfile: str = "DataLogFile.json" # BY DEFAULT

    JSONworkerObj: JSONworker = JSONworker(JSONfile)

# Checking if the specified file exists, if not, it will be created.
    if(Path(JSONfile).is_file() == False):
        JSONworkerObj.JSONfileInit()

# The array where the filtered data is entered (Cleared of parasitic fluctuations)
    sortedList: list[list[int]] = []

    while(True):

# Append data in list for defect determination operation
        try:

            try:
                deviceADCdata: list[int] = mbsSlave.getADCData()
            except Exception:

                print(colored(f"\n!!! {exMess["CommunicationErr"]} !!!\n", "red", attrs=["bold"]))

                if errorMbsWarkerLogger.readeJSONfile() == None:
                    errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while while getting ADC data")
                    errorMbsWarkerLogger.wtireErrLogJson() 
                    errorMbsWarkerLogger.clearErrBuffer()
                else:
                    for mapObj in errorMbsWarkerLogger.readeJSONfile():
                        errorMbsWarkerLogger.writeErrBuffer(mapObj['date'], mapObj['message'], mapObj['error'])
                    errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while while getting ADC data")
                    errorMbsWarkerLogger.wtireErrLogJson() 
                    errorMbsWarkerLogger.clearErrBuffer()

                mbsSlave.noComminicationHandler()
                deviceADCdata = mbsSlave.getADCData()

            statusChecker: int = parasiticConversionChecker(deviceADCdata)

            if(statusChecker == 1):
                sortedList.append(deviceADCdata)

            elif(statusChecker != 1):
                try:
                    generatedData: list[int] = mbsSlave.getGeneratedData()
                except Exception:

                    print(colored(f"\n!!! {exMess["CommunicationErr"]} !!!\n", "red", attrs=["bold"]))

                    if errorMbsWarkerLogger.readeJSONfile() == None:
                        errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while getting Final data")
                        errorMbsWarkerLogger.wtireErrLogJson() 
                        errorMbsWarkerLogger.clearErrBuffer()
                    else:
                        for mapObj in errorMbsWarkerLogger.readeJSONfile():
                            errorMbsWarkerLogger.writeErrBuffer(mapObj['date'], mapObj['message'], mapObj['error'])

                        errorMbsWarkerLogger.writeErrBuffer(str(datetime.now()), "The device is not responding", "No Communication Error while getting Final data")
                        errorMbsWarkerLogger.wtireErrLogJson() 
                        errorMbsWarkerLogger.clearErrBuffer()

                    mbsSlave.noComminicationHandler()
                    generatedData = mbsSlave.getGeneratedData()
            
                if(generatedData != dataSCBbuffer):

                    if(generatedData[0] == 1):

                        if(len(JSONworker.getDataBuffer()) != 0):

                            if(JSONworkerObj.readeJSONfile() is not None):
                                JSONworker.addDataTopInBuffer(JSONworkerObj.readeJSONfile()) # 1.Add previously written data in JSON to the Buffer

                            JSONworkerObj.writeJSONfile(JSONworker.getDataBuffer()) # 2.Overwrite JSON file with updated data
                            JSONworker.clearBuffer()# 3.Clear the Buffer
                        print(colored(f"** {genPhrases["FreeLine"]} {infoMbsDevice["sensorPoint"]} **\n", "green", attrs=["bold"]))
                    else:

                        sygnalStatus: int = DefectAnalysis(sortedList).defectDetection() # The result of determining the defect
                        sortedList.clear()

                        toSave: dict = {
                            "Direction": infoMbsDevice["sensorPoint"], 
                            "Date": f'{generatedData[0]} {months.get(generatedData[1])} {generatedData[2]} {generatedData[3]}:{generatedData[4]}:{generatedData[5]}', 
                            "Defect": defectInfo[sygnalStatus],
                            "Wheel": generatedData[6],
                            "Wagon": generatedData[7],
                            "Speed": f'{str(generatedData[8])[:len(str(generatedData[8]))-2]}.{str(generatedData[8])[len(str(generatedData[8]))-2:]}'
                        }

                        prettyOutput: str = f'{trainInfoLocal["Direction"]}: {toSave["Direction"]}\n{trainInfoLocal["Date"]}: {toSave["Date"]}\n{trainInfoLocal["Defect"]}: {toSave["Defect"]}\n{trainInfoLocal["Wheel"]}: {toSave["Wheel"]}\n{trainInfoLocal["Wagon"]}: {toSave["Wagon"]}\n{trainInfoLocal["Speed"]}: {toSave["Speed"]}\n-------------------------------\n'
                    
                        print(colored(prettyOutput, 'white', attrs=["bold"]))

                        JSONworker.addDataInBuffer(toSave) # Collecting data for saving in JSON

                    dataSCBbuffer = generatedData

        except FileNotFoundError:
            print(colored(f"!!! {exMess["DeviceErr"]} !!!!\n", "red", attrs=["bold"]))
