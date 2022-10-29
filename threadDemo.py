#! python 3.8.10
import time
import threading

print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake up')


threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program')
