import time

def countdown(total_seconds):
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timer, end="\r")  # \r to overwrite the line in terminal
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")

def main():
    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = hours * 3600 + minutes * 60 + seconds
        countdown(total_seconds)
    except ValueError:
        print("Please enter valid numbers!")

# Run the timer
if __name__ == "__main__":
    main()
