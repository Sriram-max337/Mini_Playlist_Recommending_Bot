import random
import time
import json
import os

print("Playlists-Songs Recommending Bot")

def menu():
    print("""1.Add Playlist
2.Del Playlist
3.Get Rec
4.Show all the Playlists
5.Show already recommended playlists
6.Exit""")

menu()

if not os.path.exists("Playlists.json"):
    with open("Playlists.json","w") as f:
        data = {
        "playlists": [],
        "seen": []
        }
        json.dump(data,f,indent=4)
    print("'Playlits.json' file created")

def load_data():
    with open("Playlists.json","r") as f:
        data = json.load(f) 
        return data

def save_data(data):
    with open("Playlists.json","w") as f:
        json.dump(data,f,indent=4)

def add_del_playlists(choice):
    data = load_data()

    if choice == 1:
            add_playlist = input("Enter the Playlist name to add : ")
            if add_playlist in data["playlists"]:
                print(f"'{add_playlist}' already exists in Playlists")
            else:
                data["playlists"].append(add_playlist)
                print(f"'{add_playlist}' Playlist added in Playlists")
        
    elif choice == 2:
            if data["playlists"]==[]:
                print("Enter a playlist first to remove something")
            else:
                rem_playlist = input("Enter the Playlist name to remove it : ")
                if rem_playlist in data["playlists"]:
                    data["playlists"].remove(rem_playlist)
                    print(f"'{rem_playlist}' playlist removed from the playlists")
                else:
                    print("Enter a playlist which already exists in the Playlists to remove")
    
    save_data(data)

def rec_show_playlists(choice):
    data = load_data()

    if choice == 3:
            if set(data["seen"]) == set(data["playlists"]):
                random.shuffle(data["playlists"])
                print("Playlist Shuffled by Psycho bot New-Fresh Recs...")#Dont cry i've twekaed it a lil
                data["seen"].clear()

            if data["playlists"]!=[]:
                for playlist in data["playlists"]:
                    if playlist not in data["seen"]:
                        print(f"🎧 Recommended : {playlist}")
                        data["seen"].append(playlist)
                        break
    
                save_data(data)         
            else:
                print("Playlist is empty, add some before getting recs...")
        
    elif choice == 4:
        for i,playlist in enumerate(data["playlists"]):
            print(f"{i+1} : {playlist}")
            time.sleep(0.1)

    elif choice == 5:
        if data["seen"] != []:
            print("Already Recommended Playlists")
            for i,playlist in enumerate(data["seen"]):
                print(f"{i+1} : {playlist}")
                time.sleep(0.1)
        else:
            print("No playlists Recommended yet, try getting some suggestions first")

    
        
while True:
    while True:
        try:
            choice = int(input())
            break
        except Exception:
            print()
            print("Enter an Integer")
            menu()

    if choice == 1 or choice == 2:
        add_del_playlists(choice)
    elif choice == 3 or choice == 4 or choice == 5:
        rec_show_playlists(choice)
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Enter a valid input : ")
        menu()

    time.sleep(1)
    print()
    print("What to do next?")
    menu()
        
        

