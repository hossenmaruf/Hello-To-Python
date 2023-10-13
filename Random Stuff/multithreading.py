import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


eat_breakfast()
drink_coffee()
study()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
