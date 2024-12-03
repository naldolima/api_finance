import sqlite3
from backend.core.config import settings

# filename to form database
file = settings.DB_NAME

def main():
    try:
        conn = sqlite3.connect(file)
        print(f"Database {file} formed.")
    except:
        print(f"Database {file} not formed.")

if __name__ == "__main__":
    main()
