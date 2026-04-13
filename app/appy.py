from flask import Flask, render_template
import psutil
import psycopg2
import os
import time
from datetime import datetime

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres'),
        database=os.environ.get('DB_NAME', 'metricsdb'),
        user=os.environ.get('DB_USER', 'christie'),
        password=os.environ.get('DB_PASSWORD', 'securepassword')
    )

def init_db():
    retries = 10
    while retries > 0:
        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS metrics (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP,
                    cpu FLOAT,
                    ram FLOAT,
                    disk FLOAT
                )
            ''')
            conn.commit()
            cur.close()
            conn.close()
            print("Database ready.")
            break
        except Exception as e:
            print(f"Waiting for database... {e}")
            retries -= 1
            time.sleep(3)

@app.route('/')
def dashboard():
    metrics = {
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }

    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO metrics (timestamp, cpu, ram, disk) VALUES (%s, %s, %s, %s)',
            (datetime.now(), metrics['cpu'], metrics['ram'], metrics['disk'])
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB error: {e}")

    return render_template('dashboard.html', metrics=metrics)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
