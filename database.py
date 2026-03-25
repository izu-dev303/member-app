import sqlite3

def init_db():
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_members():
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    conn.close()
    return members

def add_member(name, email):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

def delete_member(member_id):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()

def update_member(member_id, name, email):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE members SET name = ?, email = ? WHERE id = ?', (name, email, member_id))
    conn.commit()
    conn.close()