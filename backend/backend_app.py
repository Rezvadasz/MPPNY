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


@app.get("/cpu/get")
async def root():
    conn = get_db_connection()
    cur = conn.cursor()
    res = cur.execute("SELECT * FROM cpu LIMIT 10")
    cpus = res.fetchall()
    return {"cpu": [dict(cpu) for cpu in cpus]}

@app.post("/cpu/add")
async def add_cpu(cpu: models.Cpu):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO cpu (Model, PTS1, PTS2, PTS4, PTS8, PTS64, Samples) VALUES (?,?,?,?,?,?,?)", (cpu.model, cpu.PTS1, cpu.PTS2, cpu.PTS4, cpu.PTS8, cpu.PTS64, cpu.samples))
    conn.commit()
    

@app.delete("/cpu/delete/{cpu_id}")
async def delete_cpu(cpu_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM cpu WHERE id = ?", (cpu_id,))
    conn.commit()
