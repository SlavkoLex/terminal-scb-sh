# The functionality of checking the Internet connection will ensure:
# 1. Displaying a warning about its absence when setting/adjusting the time on the SCB-Sh device
# 2. Send Log files to a remote server to collect statistics and analyze them later

import requests

def checkNetConnect() -> int:

    checkAddr: list[str] = ["https://www.google.com", "https://www.yandex.com"]
    checkRes: int = 0

    for addr in checkAddr:
        try:
            if requests.get(addr).ok:
                checkRes = 1 
                break
        except Exception:
            pass

    return checkRes