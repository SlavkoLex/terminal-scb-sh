import minimalmodbus
import time

from typing import Union

class PollMbsSlave:
  
    @classmethod
    def mbsPortInit(cls,
            portName: str, 
            slvAddress: int, 
            baudrate: int, 
            bytesize: int, 
            parityBit: str, 
            countStopBits: int, 
            timeout: int
        ) -> minimalmodbus.Instrument:
        
        # absolute file path to the file that represents the ModbusRTU port,
        # slvAddress int value represents adrdress ModbusRTU Slave 

        instrument = minimalmodbus.Instrument(portName, slvAddress)

        instrument.serial.baudrate = baudrate              # Speed Send/Recive
        instrument.serial.bytesize = bytesize              # count bit in one "Word"
        instrument.serial.parity   = parityBit             # 1 Without paruty byt
        instrument.serial.stopbits = countStopBits         # 1 Stop Bit
        instrument.serial.timeout  = timeout               # Setting the time between requests to 20 ms


        return instrument
    
    
    def __init__(self, portName, slvAddress, baudrate, bytesize, parityBit, countStopBits, timeout):
        self.__slaveAddress = slvAddress
        self.__portName = portName,
        self.__mbsPort: minimalmodbus.Instrument = PollMbsSlave.mbsPortInit(
            portName, 
            slvAddress, 
            baudrate, 
            bytesize, 
            parityBit, 
            countStopBits, 
            timeout
        )

    def readMbsPortInfo(self):
        print("Baudrate: "+ str(self.__mbsPort.serial.baudrate) + "\n"+ "Port: " + 
              str(self.__portName) + "\n" + "Slave Addr. :" + str(self.__slaveAddress))
    
    def readDiscreteInput(self, addressReg: int, functionCode: int) -> int:
        return self.__mbsPort.read_bit(addressReg, functionCode)


    def readingAnalogInput(self, firstRegister: int, countRegisters: int, functionCode: int) -> Union[list[int], str]:
        return self.__mbsPort.read_registers(firstRegister, countRegisters, functionCode)
    
    def getADCData(self) -> list[int]:

        frstRgstr: int = 0 # First Register Addrres
        cntRgstr: int = 20 # Counts of Registers
        funcCode: int = 4  # Fuction Code

        return self.__mbsPort.read_registers(frstRgstr, cntRgstr, funcCode)
 

    def getGeneratedData(self) -> list[int]:

        frstRgstrFD: int = 20
        cntRgstrFD: int = 9
        funcCodeFD: int = 4
        
        return self.__mbsPort.read_registers(frstRgstrFD, cntRgstrFD, funcCodeFD)


    def getDateTime(self) -> list[int]:

        frstRgstrDT: int = 29
        cntRgstrDT: int = 6
        funcCodeDT: int = 4

        return self.__mbsPort.read_registers(frstRgstrDT, cntRgstrDT, funcCodeDT)
 

    def getAccurateSpeed(self) -> list[int]:

        frstRgstrSpd = 35
        cntRgstrSpd = 1
        funcCodeSpd = 4

        return self.__mbsPort.read_registers(frstRgstrSpd, cntRgstrSpd, funcCodeSpd)

    
    def adjustTime(self, newDateTime: list[int]):

        if(len(newDateTime) != 6):
            print("Incorrect number of arguments specified") 
        else:
            frstRgstrAT = 0
            startAdjust = 1

            newDateTime.append(startAdjust)

            self.__mbsPort.write_registers(frstRgstrAT, newDateTime)
    
    
    def noComminicationHandler(self):
        while(True):
            exFlag: int = 0

            try:
                self.getDateTime()
            except Exception:
                exFlag = 1
                time.sleep(0.5)

            if(exFlag == 0):
                break

