import sqlite3

def initialize_database():
    connection = sqlite3.connect("clinic.db")
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name TEXT NOT NULL,
            time TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


def add_appointment(doctor_name, time, first_name, last_name, phone):
    connection = sqlite3.connect("clinic.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO appointments (doctor_name, time, first_name, last_name, phone)
        VALUES (?, ?, ?, ?, ?)
    ''', (doctor_name, time, first_name, last_name, phone))

    connection.commit()
    connection.close()


def get_appointments():
    connection = sqlite3.connect("clinic.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()

    connection.close()
    return appointments