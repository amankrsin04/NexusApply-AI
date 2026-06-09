import sqlite3

def init_db(config):

    conn = sqlite3.connect(
        config["database"]["name"]
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        link TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()


def save_job(config, job):

    conn = sqlite3.connect(
        config["database"]["name"]
    )

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO jobs (title, company, link)
        VALUES (?, ?, ?)
        """, (
            job["title"],
            job["company"],
            job["link"]
        ))

        conn.commit()

    except:
        pass

    conn.close()
