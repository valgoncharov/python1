import sqlite3


DB_NAME = "sqlite_db.db"

courses = [
    (199, "Java courses", 10, 5),
    (235, "C# courses", 40, 120),
    (224, "C++ courses", 78, 55)
]
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
    for course in courses:
        sqlite_conn.execute(sql_request, course)
    sqlite_conn.commit()
