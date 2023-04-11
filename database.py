from sqlalchemy import create_engine,text

db_connection_string = "mysql+pymysql://qg2tx2ijpig1bwa6gu6a:pscale_pw_Ow4hUvsaf6SZzDhhvjOidoYOK5YAqzCZLEsL68gMtbW@aws.connect.psdb.cloud/chinyemba?charset=utf8mb4" 

engine = create_engine(db_connection_string,    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    })


