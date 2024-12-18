import os
import time
import pandas

while True:
    if os.path.exists(
        "c:/Users/pato1/OneDrive/Documentos/PythonMegaCourse/modules/module 12/temps_today.csv"
    ):
        data = pandas.read_csv(
            "c:/Users/pato1/OneDrive/Documentos/PythonMegaCourse/modules/module 12/temps_today.csv"
        )
        print(time.strftime("%H:%M:%S"))
        print(data.mean())
    else:
        print("File not found")
        break
    print("/---------------/")
    time.sleep(10)
