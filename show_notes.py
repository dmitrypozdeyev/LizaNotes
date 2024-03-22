import json
from datetime import datetime
from tkinter import Label, Tk

try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = []
    
    
def get_notes_by_date(notes: list, date: str) -> list:
    notes_date = []
    for note in notes:    
        if note["date"] == date:
            notes_date.append(note)
    notes_date.sort(key=lambda note: note["imp"], reverse=True)        
    return notes_date

now = datetime.now().strftime("%d.%m.%Y")

window = Tk()
window.title("Заметки на сегодня")
Label(text=f"Заметки на сегодня: {now}", font=("dejavubold",20)).pack()
for note in get_notes_by_date(notes, now):
    Label(text=f"Текст: {note['text']}, дата: {note['date']}, важность: {note['imp']}").pack(anchor="w")
    
    
window.mainloop()