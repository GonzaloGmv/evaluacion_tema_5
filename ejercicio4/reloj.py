import datetime
import time
from os import system

# la linea 8 la he tenido que buscar en internet tal cual está
while True:
    system("cls")
    print(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(1)