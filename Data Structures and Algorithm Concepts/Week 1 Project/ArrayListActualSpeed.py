#Name: Faith Burnett
#Date:  04/17/2024

from ArrayList import ArrayList
from Client import Client
from Quicksort import Quicksort
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
    Quicksort.sort(clients)
    return clients

def addClientsSpeed(clientList, clientArray):
    
    start_time = time.time()
    
    for i in range(len(clientList)):
        clientArray.append(clientList[i])
    
    end_time = time.time()

    elapsed_time = end_time - start_time
    
    print(f"Time taken to add {len(clientList)} Client objects to ArrayList: {elapsed_time} seconds\n")

def removeClientsSpeed(clientList, clientArray):
    
    start_time = time.time()
    
    for i in range(len(clientList)):
        clientArray.remove_at(0)  
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
        
    
    print(f"Time taken to remove {len(clientList)} Client objects from ArrayList: {elapsed_time} seconds\n")

def getRandomRecords(clientList, clientArray):
    
    start_time = time.time()
    
    for i in range(1000):
        min_id = 100001
        max_id = min_id + len(clientList)
        r_num = random.randint(min_id, max_id)
        print(clientArray.search_sorted(Client(r_num)))
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"\nTime taken to get a random number of Client objects from ArrayList:\n{elapsed_time} seconds")

def addDisplayRemoveSpeed(clientList, clientArray):
    
    r_num = random.randint(0, 100001)
    start_time = time.time()

    print("Adding clients...\n")
    
    #add client
    for i in range(len(clientList)):
        clientArray.append(clientList[i])
    
    print("Displaying random clients...\n") 
    
    #display random clients
    for r_num in range(1000):
        min_id = 100001
        max_id = min_id + len(clientList)
        r_num = random.randint(min_id, max_id)
        print(clientArray.search_sorted(Client(r_num)))

    print("\n")

    #remove random clients
    for r_num in range(1000):
        clientArray.remove_at(r_num)
        
    print("Removing random clients...\n")
    
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Time taken to add, display and delete client objects in ArrayList:\n{elapsed_time} seconds\n")

if __name__ == "__main__":
    
    nameAndDate()
    
    file_path = 'ClientData.csv'
    client_list = read_clients_from_csv(file_path)
    
    client_array = ArrayList()
    
    # addClientsSpeed(client_list, client_array)
        
    # removeClientsSpeed(client_list, client_array)
    
    # getRandomRecords(client_list, client_array)
    
    addDisplayRemoveSpeed(client_list, client_array)
    
    
    
    