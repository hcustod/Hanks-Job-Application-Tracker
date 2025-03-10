import sqlite3

def setup_db():
    conn = sqlite3.connect('jobs_main.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS job_applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_title TEXT NOT NULL,
        company TEXT NOT NULL,
        location TEXT,
        work_type TEXT,
        job_type TEXT,
        salary TEXT,
        posting_date TEXT,
        applied_date TEXT,
        status TEXT,
        notes TEXT,
        job_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_jobs():
    conn = sqlite3.connect('jobs_main.db')
    c = conn.cursor()
    c.execute("SELECT id, job_title, company, location, status, applied_date FROM job_applications")
    jobs = c.fetchall()
    conn.close()
    return jobs

def add_job(job_title, company, location, status, application_date, notes):
    conn = sqlite3.connect('jobs_main.db')
    c = conn.cursor()
    c.execute("INSERT INTO job_applications (job_title, company, location, status, applied_date, notes) VALUES (?, ?, ?, ?, ?, ?)",
                   (job_title, company, location, status, application_date, notes))
    conn.commit()
    conn.close()

def delete_job(job_id):
    conn = sqlite3.connect('jobs_main.db')
    c = conn.cursor()
    c.execute("DELETE FROM job_applications WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()



