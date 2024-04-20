#Name: Faith Burnett    
#Date: 3/23/2024

from Client import Client
from BubbleSort import BubbleSort
from InsertionSort import InsertionSort
from MergeSort import MergeSort
from Quicksort import Quicksort
from SelectionSort import SelectionSort
from ShellSort import ShellSort
from datetime import date
import time

def nameAndDate():
    baseDate = date.today()
    today = baseDate.strftime('%B %d, %Y')
    print(f"Name: Faith Burnett\nDate: {today}\n")
    
def read_clients_to_file(filepath):
    clients = []
    with open(filepath) as infile:
        for line in infile:
            s = line.split(',')
            client_id = int(s[0])
            client_fname = s[1]
            client_lname = s[2]
            client_phone = s[3]
            client_email = s[4]
            client = Client(client_id, client_fname, client_lname, client_phone, client_email)
            clients.append(client)
        return clients
    
    
if __name__ == "__main__":
    nameAndDate()
    
    # client_list = read_clients_to_file("ClientData100.csv")
    # client_list = read_clients_to_file("ClientData1000.csv")
    # client_list  = read_clients_to_file("ClientData10000.csv")
    client_list = read_clients_to_file("ClientData100000.csv")
    
    num_records = len(client_list)

    print("Sorting " +  str(num_records) + " records...")
    
    start_time = time.time()

    MergeSort.sort(client_list)

    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print("Seconds to sort " + str(num_records) + " records " + str(elapsed_time) + "\n")
    
    # for client in client_list:
    #     print(client)
        
        