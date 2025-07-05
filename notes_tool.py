import subprocess
import time
import os
import psycopg2
from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
import webbrowser
from utils.get_connection import get_connection

class NoteInput(BaseModel):
    title: str
    content: Optional[str] = None

class NoteOutput(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime



def start_notes_app() -> str:
    try:
        workdir = os.path.abspath(".")  # kendi yolun
        print(f"Çalışma dizini: {workdir}")
        result=subprocess.run(
            ["docker", "compose", "up", "-d"],
            cwd=workdir,
            
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print(result.stderr)
        print(result.stdout)

        webbrowser.open("http://localhost:8001")  # Siteyi varsayılan tarayıcıda aç
        return "Not uygulaması başlatıldı ve tarayıcıda açıldı."
    except subprocess.CalledProcessError as e:
        return f"Başlatma hatası: {e.stderr}"




# def is_db_container_running() -> bool:
#     try:
#         result = subprocess.run(
#             ["docker", "ps", "--filter", "name=postgres_db", "--format", "{{.Names}}"],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
            
#         )
#         return "postgres_db" in result.stdout.strip()
#     except subprocess.CalledProcessError:
#         return False
    



# def start_db_container():
#     workdir = os.path.abspath(".")

#     docker_path = r"C:\Program Files\Docker\Docker\resources\bin\docker.exe"
#     print(f"Docker yolu: {docker_path}")
#     result = subprocess.run(
#         [docker_path, "compose","-f", "compose.yaml", "up","-d", "db"],
#         cwd="C:\\Users\ms\u0131\\Desktop\\baba-projeler\\Basic-GenAI-Projects\\personal_assistant",
#         stdout=subprocess.PIPE, 
#         stderr=subprocess.PIPE,
#         text=True,
#     )
#     print(result.stdout)
#     print(result.stderr)
#     print(result.returncode)


def add_note(input: NoteInput) -> str:

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes_note (title, content, created_at) VALUES (%s, %s, NOW())",
            (input.title, input.content)
        )
        conn.commit()
        cur.close()
        conn.close()
        return f"Not eklendi: {input.title}"
    except psycopg2.OperationalError as e:
        return f"Hata: Veritabanına bağlanılamadı. {str(e)}"

def list_notes(limit: int = 5) -> List[NoteOutput]:
    
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT title, content, created_at FROM notes_note ORDER BY created_at DESC LIMIT %s", (limit,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [NoteOutput(title=r[0], content=r[1], created_at=r[2]) for r in rows]
    except psycopg2.OperationalError as e:
        raise Exception(f"Hata: Veritabanına bağlanılamadı. {str(e)}")
if __name__ == "__main__":
 pass