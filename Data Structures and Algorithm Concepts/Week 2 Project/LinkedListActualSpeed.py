#Name: Faith Burnett    
#Date: 04/20/2024

from LinkedList import LinkedList
from Client import Client
from datetime import date
import time, random

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
            first_name = s[1]
            last_name = s[2]
            phone = s[3]
            email = s[4]
            clt = Client(client_id, first_name, last_name, phone, email)
            clients.append(clt)
        return clients

def addClients(clientList, linkedList):
    start_time = time.time()
    
    for i in range(len(clientList)):
        linkedList.add_last(clientList[i])
        
    end_time = time.time()
        
    elapsed_time = end_time - start_time

    print(f"Time taken to add {len(clientList)} Client objects to LinkedList: {elapsed_time} seconds\n")

def removeClients(clientList, linkedList):
    start_time = time.time()
        
    for i in range(len(clientList)):
        linkedList.remove_first()
            
    end_time = time.time()
        
    elapsed_time = end_time - start_time
        
    print(f"Time taken to remove {len(clientList)} Client objects from LinkedList: {elapsed_time} seconds\n")
    
def displayRandom(clientList, linkedList):
    start_time = time.time()
        
    for i in range(1000):
        small_id = 100001
        large_id = small_id + len(clientList)
        random_num = random.randint(small_id, large_id)
        print(linkedList.search(Client(random_num)))
            
    end_time = time.time()
        
    elapsed_time = end_time - start_time
        
    print(f"Time taken to get 1000 random Client objects from LinkedList: {elapsed_time} seconds\n")

def addDisplayRemove(clientList, linkedList):
    
    start_time = time.time()
        
    for i in range(len(clientList)):
        linkedList.add_last(clientList[i])
        
    print("Adding clients...\n")
    
    print("Displaying clients...\n")
    for i in range(1000):
        small_id = 100001
        large_id = small_id + len(clientList)
        random_num = random.randint(small_id, large_id)
        print(linkedList.search(Client(random_num)))

    print("\nRemoving clients...")
    for i in range(1000):
        small_id = 100001
        large_id = small_id + len(clientList)
        random_num = random.randint(small_id, large_id)
        linkedList.remove(Client(random_num))
        
        
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Time taken to get clients added, grab random clients and remove random clients: {elapsed_time} seconds\n")
    
if __name__ == "__main__":
    
    nameAndDate()
    
    client_list = read_clients_to_file('ClientData.csv')
    linked_list = LinkedList()
    
    addDisplayRemove(client_list, linked_list)
    
    
    # addClients(client_list, linked_list)
    # displayRandom(client_list, linked_list)
    
    # addDisplayRemove(client_list, linked_list)
    # addClients(client_list, linked_list)
    # removeClients(client_list, linked_list)