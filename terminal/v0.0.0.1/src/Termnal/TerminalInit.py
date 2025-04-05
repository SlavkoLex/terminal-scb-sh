def terminalInit(terminalLocal: dict) -> dict:
             
    fileName: str = input(f"** {terminalLocal["LogFile"]} -> ")
    portPath: str = input(f"** {terminalLocal["Port"]} -> ")                           
    addressSlave: str = input(f"** {terminalLocal["Address"]} -> ")                                     
    sensorPoint: str = input(f"** {terminalLocal["Destination"]} -> ")

    return dict(fileName=fileName, portPath=portPath, addressSlave=addressSlave, sensorPoint=sensorPoint)