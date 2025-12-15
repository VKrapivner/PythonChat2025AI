import tkinter as tk
import pymongo

# MongoDB setup
#Skapa klient

#client = pymongo.MongoClient("mongodb://localhost:27017") #skapar kopling mellan app.py och mongodb
client = pymongo.MongoClient("mongodb+srv://Vera:Viggo2012@pychat.ete8qzm.mongodb.net/?appName=PyChat")#skapar client till molnet
db = client["PyChat"] #Skapar en ny db, för att skapa en ny db behöver även en collection name anges
messages_collection = db["messages"] #skapar en collection i db 

#Dessa 3 rader kod behövs för att skapa en koppling till Mondo DB 

root = tk.Tk()
root.title("MongoChatt")
root.geometry("800x800")

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

def send_message():
    if entry.get():
        messages_collection.insert_one({"text": entry.get()})#vill skicka in objekt text
        entry.delete(0, tk.END)#tar bort från den första karraktären till den sista karraktären i rutan

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

#Message label för läsning av messages

message_label = tk.Label(root, text="Messages: ", justify="left")
message_label.pack()

def fetch_messages():
    messages = messages_collection.find().sort("_id")#där id är nyckeln från MongoDB
    message_label.config(text="Messages: \n" + "\n".join(f" - {m['text']}" for m in messages))
    root.after(2000, fetch_messages)#kör den varje 2 sekunder

fetch_messages()#kallar på def fetch_messages från start
root.mainloop()

#Visuella Github instruktioner 
#Steg 1, Tryck på source control ikonen till vänster
#Steg 2, Append changes
#Steg 3, Skriv en kommentar
#Steg 4, Tryck på commit

#Terminal kommandon för Github
#Steg 1, git status - visar förändringar 
#Steg 2, git add . - lägger till ändringar under changes, git add app.py lägger till bara den specifika filen
#Steg 3, git commit -m "comment for commit"
#Steg 4, git push 