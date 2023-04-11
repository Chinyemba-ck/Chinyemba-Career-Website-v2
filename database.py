from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string,
                      connect_args={
                            "ssl": {
                              "ssl_ca": "/etc/ssl/cert.pem"  
                            }
                      } 
                       )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.fetchall():
            jobs.append(dict(row._asdict()))
        return jobs



