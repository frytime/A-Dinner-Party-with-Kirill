from threading import Timer
def times_out():
    print("You have run out of time")
t = Timer(10, times_out)
t.start()
t.join()