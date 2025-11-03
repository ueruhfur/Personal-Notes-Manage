from pathlib import Path

DATA_FILE = Path("data/notes.txt")

def save_note(text):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\\n")

def load_notes():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def remove_note(index):
    notes = load_notes()
    if 0 < index <= len(notes):
        del notes[index - 1]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.writelines(notes)
