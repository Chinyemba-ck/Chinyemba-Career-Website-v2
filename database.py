from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "mysql+pymysql://pb3rh9keh9neauebb0lh:pscale_pw_WzFD2RwClt0ggV3dVuyM25F1eObhx7xacM6a2UecMec@aws.connect.psdb.cloud/chinyemba?charset=utf8mb4"
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



