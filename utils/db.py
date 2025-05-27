import sqlite3
from datetime import datetime

def init_db():
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    # Таблица для расписания (путь к фото)
    sql.execute("""CREATE TABLE IF NOT EXISTS canteen_menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT UNIQUE,
        photo_path TEXT,
        timestamp TEXT
    )""")
    # Таблица для анонимных сообщений
    sql.execute("""CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message TEXT,
        timestamp TEXT
    )""")
    # Таблица админов
    sql.execute("""CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        admin_id INTEGER
    )""")
    db.commit()
    db.close()

def save_canteen_menu(date: str, photo_path: str):
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    sql.execute("INSERT OR REPLACE INTO canteen_menu (date, photo_path, timestamp) VALUES (?, ?, ?)",
              (date, photo_path, datetime.now().isoformat()))
    db.commit()
    db.close()

def get_canteen_menu(date: str = None) -> str:
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    sql.execute("SELECT photo_path FROM canteen_menu WHERE date = ?", (date,))
    result = sql.fetchone()
    db.close()
    return result[0] if result else None

def save_anonym_message(message: str, user_id: int):
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    sql.execute("INSERT INTO messages (user_id, message, timestamp) VALUES (?, ?, ?)",
              (user_id, message, datetime.now().isoformat()))
    db.commit()
    db.close()

def admins_get():
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    sql.execute("SELECT admin_id FROM admins")
    result = sql.fetchall()
    db.close()
    return list(x[0] for x in result)

def admin_add(admin_id: str):
    db = sqlite3.connect("data/database.db")
    sql = db.cursor()
    sql.execute("INSERT INTO admins (admin_id) VALUES (?,)",
              (admin_id))
    db.commit()
    db.close()

if __name__ == '__main__':
    try:
        print(admins_get())
    except KeyboardInterrupt:
        print('Exit')