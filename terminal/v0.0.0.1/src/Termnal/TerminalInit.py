def terminalInit(terminalLocal: dict) -> dict:
             
    portPath: str = input(f"** {terminalLocal["Port"]} -> ")                           
    addressSlave: str = input(f"** {terminalLocal["Address"]} -> ")                                     
    sensorPoint: str = input(f"** {terminalLocal["Destination"]} -> ")

    return dict(portPath=portPath, addressSlave=addressSlave, sensorPoint=sensorPoint)