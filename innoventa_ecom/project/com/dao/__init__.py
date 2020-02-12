import pymysql
from sqlalchemy import create_engine


def con_db():
    engine = create_engine('mysql+pymysql://root:root@localhost:3306/innoventa')
    return engine

import project.com.dao
