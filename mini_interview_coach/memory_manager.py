import json 
import os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "interview_memory.json")




if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE,"w") as f:
        json.dump({"history":[]},f)

def save_to_memory(question,answer,feedback):
    "save user+ agent messages into long term memory"
    with open(MEMORY_FILE,"r") as f:
        data=json.load(f)
    data["history"].append({
        "Question":question,
        "Answer":answer,
        "Feedback":feedback
    })
    with open(MEMORY_FILE,"w") as f:
        json.dump(data,f,indent=4)

def get_recent_memory(n=3):
    "retrieve last memory"
    with open(MEMORY_FILE,"r") as f:
        data=json.load(f)
    return data["history"][-n:]