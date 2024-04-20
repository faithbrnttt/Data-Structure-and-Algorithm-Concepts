#Name: Faith Burnett
#Date:  04/06/2024

from Client import Client
from BinarySearchTree import BinarySearchTree
from datetime import date
import time, random

def nameAndDate():
    baseDate = date.today()
    today = baseDate.strftime('%B %d, %Y')
    print(f"Name: Faith Burnett\nDate: {today}\n")

def read_clients_from_csv(file_path):
    clients = []
    with open(file_path) as infile:
        for line in infile:
            s = line.split(',')
            client_id = int(s[0])
            first_name = s[1]
            last_name = s[2]
            phone = s[3]
            email = s[4]
            clt = Client(client_id, first_name, last_name, phone, email)
            clients.append(clt)
    return clients

def add_clients(clientList, binarySearch):
    start_time = time.time()
    
    for client in range(len(clientList)):
        binarySearch.insert(clientList[client]) 
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Seconds to add records {elapsed_time}.")
    
def remove_clients(clientList, binarySearch):
    start_time = time.time()
    
    for client in range(len(clientList)):
        binarySearch.remove_minimum() 
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Seconds to remove records {elapsed_time}.")

def display_random_clients(clientList, binarySearch):
    start_time = time.time()
    
    for client in range(1000):
        small_id = 100001
        large_id = small_id + len(clientList)
        rand = random.randint(small_id, large_id)
        print(binarySearch.search(Client(rand))) 
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Seconds to display 1000 random records {elapsed_time}.")

def add_remove_display_clients(clientList, binarySearch):
    start_time = time.time()
    
    add_clients(clientList, binarySearch)
    display_random_clients(clientList, binarySearch)
    
    for client in range(1000):
        small_id = 100001
        large_id = small_id + len(clientList)
        rand = random.randint(small_id, large_id)
        binarySearch.remove(Client(rand))
        
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Seconds to add, randomly display and randomly remove clients {elapsed_time}.")
    
if __name__ == "__main__":
    nameAndDate()
    file_path = 'ClientData.csv'
    client_list = read_clients_from_csv(file_path)

    bst = BinarySearchTree()
    
    add_remove_display_clients(client_list, bst)
    