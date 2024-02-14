import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

countdown_time = int(input("Enter the countdown time in "))
countdown_timer(countdown_time)
