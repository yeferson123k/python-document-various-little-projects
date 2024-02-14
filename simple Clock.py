from multiprocessing import current_process
import time 

def digital_clock():
    while True:       
        current_time =time.strftime("%H:%M:%S")
        print(current_time, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    try:
        digital_clock()
    except KeyboardInterrupt:
        print("\nClock Stopped!")