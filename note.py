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

def delete_note(note_hash):
    ensure_db()
    file_path = os.path.join(DB_DIR, note_hash)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted note: {note_hash}")
    else:
        print(f"Error: Note with hash {note_hash} not found.")

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
    elif command == "delete":
        if len(args) < 2:
            print("Usage: note delete <hash>")
        else:
            delete_note(args[1])
