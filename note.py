import sys
import os
import hashlib

DB_DIR = os.path.join(".notes", "db")

def ensure_db():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

def add_note(text):
    ensure_db()
    note_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    file_path = os.path.join(DB_DIR, note_hash)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Note saved with hash: {note_hash}")

def list_notes():
    ensure_db()
    files = os.listdir(DB_DIR)
    if not files:
        print("No notes found.")
        return
    for note_hash in files:
        file_path = os.path.join(DB_DIR, note_hash)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        print(f"{note_hash} -> {content}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: note [add|list|delete]")
        sys.exit(1)
        
    command = args[0]
    if command == "add":
        if len(args) < 2:
            print("Usage: note add <text>")
        else:
            add_note(" ".join(args[1:]))
    elif command == "list":
        list_notes()
