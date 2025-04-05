# The function allows you to filter out spurious transformations.
def parasiticConversionChecker(array: list[int]) -> int:
   
    PARASITIC_CONVERSION_VALUE = 20 # 50 -> The value that can be obtained as a result of a parasitic transformation (Established experimentally)

    oneMoreCounter: int = 0
    for arg in array:
        if(arg > PARASITIC_CONVERSION_VALUE): 
            oneMoreCounter += 1
            break
    return oneMoreCounter