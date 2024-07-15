import sqlite3
from datetime import datetime

DATABASE_NAME = 'submissions.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,
        code TEXT NOT NULL,
        submission_date TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fingerprints (
        id INTEGER PRIMARY KEY,
        submission_id INTEGER,
        position INTEGER,
        hash INTEGER,
        FOREIGN KEY (submission_id) REFERENCES submissions (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def save_submission(filename, code, fingerprints):
    conn = get_db_connection()
    cursor = conn.cursor()
    submission_date = datetime.now().isoformat()
    try:
        cursor.execute('INSERT INTO submissions (filename, code, submission_date) VALUES (?, ?, ?)', 
                       (filename, code, submission_date))
        submission_id = cursor.lastrowid
        cursor.executemany('INSERT INTO fingerprints (submission_id, position, hash) VALUES (?, ?, ?)',
                           [(submission_id, position, hash_value) for position, hash_value in fingerprints])
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_all_submissions():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT id, filename, submission_date FROM submissions ORDER BY submission_date DESC')
        submissions = cursor.fetchall()
        return submissions
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()