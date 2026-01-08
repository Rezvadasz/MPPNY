from fastapi import FastAPI
import sqlite3
from pathlib import Path
import models

app = FastAPI()


def get_db_connection():
    script_dir = Path(__file__).parent
    db_path = script_dir.parent / "database" / "database.db"
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    return con



@app.post("/user/add")
async def add_user(user: models.User):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user (name) VALUES (?)", (user.name,))
    conn.commit()
    return "DONE!"
    


@app.get("/user/get")
async def root():
    conn = get_db_connection()
    cur = conn.cursor()
    res = cur.execute("SELECT id, name FROM user")
    return res

