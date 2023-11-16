import sqlite3

class NotesApp:
    def __init__(self, db_name='notes.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT
            )
        ''')
        self.conn.commit()

    def add_note(self, title, content):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        self.conn.commit()

    def view_notes(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM notes')
        notes = cursor.fetchall()
        for note in notes:
            print(f"ID: {note[0]}, Title: {note[1]}, Content: {note[2]}")

    def delete_note(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Contoh penggunaan aplikasi
if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nMenu:")
        print("1. Tambah Catatan")
        print("2. Lihat Catatan")
        print("3. Hapus Catatan")
        print("4. Keluar")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            title = input("Masukkan judul catatan: ")
            content = input("Masukkan isi catatan: ")
            app.add_note(title, content)
            print("Catatan ditambahkan!")

        elif choice == '2':
            print("\nDaftar Catatan:")
            app.view_notes()

        elif choice == '3':
            note_id = input("Masukkan ID catatan yang ingin dihapus: ")
            app.delete_note(note_id)
            print("Catatan dihapus!")

        elif choice == '4':
            app.close_connection()
            print("Aplikasi ditutup.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
