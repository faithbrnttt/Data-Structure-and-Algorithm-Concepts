#Name: Faith Burnett    
#Date: 04/20/2024

from Queue import Queue
from Call import Call
from datetime import date
import time
import random

def nameAndDate():
    baseDate = date.today()
    today = baseDate.strftime('%B %d, %Y')
    print(f"Name: Faith Burnett\nDate: {today}\n")
    
def read_clients_from_file(filepath):
    calls = []
    with open(filepath) as infile:
        for line in infile:
            s = line.split(',')
            client_id = int(s[0])
            client_name = s[1]
            client_phone = s[2]
            call = Call(client_id, client_name, client_phone)
            calls.append(call)
        return calls
    
def event1(callList, callsWaiting, callNumber):
    print("Call received. Caller added to queue.")
    rand = random.randint(0, len(callList))
    callsWaiting.enqueue(callList[rand])    
    callNumber += 1
                
    print("\tNumber of calls waiting in queue:", callsWaiting.get_length())

def event2(callsWaiting):
    print("Call sent to representative for service.")
    if callsWaiting.get_length() > 0: 
        print("Caller information:")
        print(callsWaiting.dequeue())
    else:
        print("The call waiting queue is empty.")
        print("\tNumber of calls waiting in queue:", callsWaiting.get_length())
    
if __name__ == "__main__":
    nameAndDate()
    call_list = read_clients_from_file('CallsData.csv')
    calls_waiting = Queue()
    call_number = 0
    
    seconds = int(input("How many seconds do you want to simulate? "))
    
    for i in range(seconds):
        print(".........................................................")
        time.sleep(2)
        rand_num = random.randint(1, 3)
        
        if rand_num == 1:
            event1(call_list, calls_waiting, call_number)
            
        elif rand_num == 2:
            event2(calls_waiting)
            
        else:
            print("Nothing happened during this second in time.")
            print("\tNumber of calls waiting in queue:", calls_waiting.get_length())
            
    print("\nThe 'Automatic Call Distributor' simulation has completed.")
    
    
    