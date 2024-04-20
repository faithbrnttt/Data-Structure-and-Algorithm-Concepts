#Name: Faith Burnett
#Date:  04/11/2024
import time    # use time library to time the code executions
from datetime import date # use datetime library to display current date in output

# display name and date in output
def nameAndDate():
    baseDate = date.today()
    today = baseDate.strftime('%B %d, %Y')
    print(f"Name: Faith Burnett\nDate: {today}\n")

# output phrase 1000 times
def phraseOutputSpeed():
    # get current time before the process
    start_time = time.time()

    # run the process
    for i in range(1000):
        print( "Hello Everyone!" )

    # get current time after the process
    end_time = time.time()

    # subtract start time from end time to get time used by process
    elapsed_time = end_time - start_time

    # Show the result.  Note: .6f means “show six decimal places”
    print(f"Seconds to run phrase 1000 times: {elapsed_time}") 

if __name__ == "__main__":
    nameAndDate()
    phraseOutputSpeed()