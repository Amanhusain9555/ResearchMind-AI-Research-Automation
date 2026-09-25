import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
#######
import psycopg2

"""conn = psycopg2.connect(
    host="localhost",
    database="Research_mind",
    user="postgres",
    password="sayyed",
    port="5432"
)"""
conn = psycopg2.connect(
    host=os.getenv("SUPABASE_DB_HOST"),
    port=os.getenv("SUPABASE_DB_PORT"),
    database=os.getenv("SUPABASE_DB_NAME"),
    user=os.getenv("SUPABASE_DB_USER"),
    password=os.getenv("SUPABASE_DB_PASSWORD")
)
cursor = conn.cursor()

# table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id SERIAL PRIMARY KEY,
    topic TEXT,
    report TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()


# save data
def save_report(topic, report, feedback):
    try:
        print("Saving:", topic)

        cursor.execute(
            """
            INSERT INTO history (topic, report, feedback)
            VALUES (%s, %s, %s)
            """,
            (topic, report, feedback)
        )

        conn.commit()
        print("Saved successfully!")

    except Exception as e:
        print("DB ERROR:", e)

# get history
def get_history():
    cursor.execute(
        "SELECT topic, created_at FROM history ORDER BY id DESC"
    )
    return cursor.fetchall()

def get_all_history():
    cursor.execute(
        """
        SELECT id, topic, created_at
        FROM history
        ORDER BY id DESC
        """
    )
    return cursor.fetchall()

def get_history_by_id(chat_id):
    cursor.execute(
        """
        SELECT topic, report, feedback
        FROM history
        WHERE id = %s
        """,
        (chat_id,)
    )
    return cursor.fetchone()

print("Database Ready!")