import sqlite3

def create_database_tables():
    con = sqlite3.connect("cgi-bin/software_database.db")
    cursor = con.cursor()

    # Создание таблицы Software
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Abonement (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Age TEXT NOT NULL,
            Trener TEXT NOT NULL,
            Description TEXT
        )
    """)

    # Создание таблицы Releases
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Zapis (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TrenerID INTEGER NOT NULL,
            ReleaseDate TEXT NOT NULL,
            FOREIGN KEY (TrenerID) REFERENCES Abonement(ID)
        )
    """)

    # Создание таблицы Developers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Trener (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL
        )
    """)

    con.commit()
    con.close()

def select_data_from_tables():
    con = sqlite3.connect("cgi-bin/software_database.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM Software")
    software = cursor.fetchall()

    cursor.execute("SELECT * FROM Releases")
    releases = cursor.fetchall()

    cursor.execute("SELECT * FROM Developers")
    developers = cursor.fetchall()

    con.close()

    return software, releases, developers

def main():
    create_database_tables()
    software, releases, developers = select_data_from_tables()

    print("Content-type: text/html\n")  # Добавлен заголовок Content-type для правильной работы CGI

    print("<html>")
    print()
    print("<head><meta charset=\"UTF-8\"><link rel=\"stylesheet\" href=\"../style.css\"><title>Tablici</title></head>")
    print("<div class=\"flex-div\"><table><tr><th colspan=\"4\">Abonement</th></tr><tr><th>ID</th><th>FIO</th><th>Age</th><th>Trener</th><th>Dop information</th></tr>")
    for software_row in software:
        print(f"<tr><td>{software_row[0]}</td><td>{software_row[1]}</td><td>{software_row[2]}</td><td>{software_row[3]}</td><td>{software_row[4]}</td></tr>")
    print("</table>")
    print("<table><tr><th colspan=\"2\">Date zanatiya</th></tr><tr><th>Trener ID</th><th>Data reliza</th></tr>")
    for release_row in releases:
        print(f"<tr><td>{release_row[1]}</td><td>{release_row[2]}</td></tr>")
    print("</table>")
    print("<table><tr><th colspan=\"2\">Trener</th></tr><tr><th>ID</th><th>Imya</th></tr>")
    for developer_row in developers:
        print(f"<tr><td>{developer_row[0]}</td><td>{developer_row[1]}</td></tr>")
    print("</table></div>")
    print()
    print("<div class=\"flex-div\"><a href=\"../index.html\">Nazad</a></div>")
    print()
    print("<div class=\"flex-div\"><a href=\"load-json.py\">Tablici v JSON</a></div>")
    print()
    print("</html>")

if __name__ == "__main__":
    main()