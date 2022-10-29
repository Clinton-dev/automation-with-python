#! python 3.8.10
import time


def calcProd():
    # calc product of the first 100, 000 numbers
    product = 1

    for i in range(1, 100_000):
        product = product * i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('The code took %s seconds to run' % (endTime - startTime))
