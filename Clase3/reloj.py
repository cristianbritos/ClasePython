
import time
from datetime import datetime
import sys

try:
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")
        print("\rHora Actual: {}".format(ahora), end="")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
    sys.exit()
