from sqlalchemy import create_engine
from sqlalchemy import text


db_connection_string = DB_CONNECTION_STR

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


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"),
            {"id": id}
        )

    row = result.fetchone()
    if row is None:
        return None
    else:
        # Define the column names as a tuple
        column_names = ('id', 'title', 'location', 'salary', 'currency', 'responsibilities', 'requirements', 'created_at', 'updated_at')

        # Use zip() to combine the column names and data into a dictionary
        job_dict = dict(zip(column_names, row))
        job_dict.pop('created_at', None)
        job_dict.pop('updated_at', None)

        # Return the resulting dictionary
        return job_dict