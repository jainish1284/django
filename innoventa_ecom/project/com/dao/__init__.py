import pymysql
from sqlalchemy import create_engine


def con_db():
    engine = create_engine('mysql+pymysql://root@root:localhost/innoventa')
    return engine

import project.com.dao
