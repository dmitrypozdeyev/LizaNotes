from tkinter import Tk, Label, Entry, ttk, Button
from tkcalendar import DateEntry
import json
note = {}
imp_vars = [i for i in range(1, 11)]

window = Tk()
window.title("Добавление заметки")
window.geometry("300x100")
note_text_label = Label(text="Текст заметки", font=("dejavubold",))
note_text_label.grid(row=0, column=0)
note_text_entry = Entry()
note_text_entry.grid(row=0, column=1)
note_date_Label = Label(text="Дата")
note_date_entry = DateEntry()
note_date_Label.grid(row=1, column=0)
note_date_entry.grid(row=1, column=1)
note_imp_Label = Label(text="Важность")
note_imp_cb = ttk.Combobox(values=imp_vars)
note_imp_Label.grid(row=2, column=0)
note_imp_cb.grid(row=2, column=1)
def save_note():
    with open("notes.json", "r") as file:
        notes = json.load(file)
    note["text"] = note_text_entry.get()
    note["date"] = note_date_entry.get()
    note["imp"] = int(note_imp_cb.get())
    notes.append(note)
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
note_save_btn = Button(text="Добавить", command=save_note)
note_save_btn.grid(row=3, column=1)




if __name__ == "__main__":
    window.mainloop()