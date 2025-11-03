from src.storage import save_note, load_notes, remove_note
from src.utils.helper import divider

def add_note(text):
    save_note(text)
    print("Note added successfully!")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    print(divider("Your Notes"))
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note.strip()}")

def delete_note(index):
    remove_note(index)
    print("Note deleted.")
