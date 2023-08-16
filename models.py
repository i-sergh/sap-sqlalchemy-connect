from sqlalchemy import Column, VARCHAR, Integer
from hanadb import Base as  HanaBase
from pgdb import Base as PgBase

class HanaMARA(HanaBase):
    __tablename__ = 'MARA'
    __table_args__ = {'schema': 'ABAPS417'}
   # id = Column(Integer, primary_key=True)
    MANDT = Column(VARCHAR, primary_key=True)
    MATNR = Column(VARCHAR, primary_key=True)
    ERSDA = Column(VARCHAR)
    ERNAM = Column(VARCHAR)
    LAEDA = Column(VARCHAR)
    AENAM = Column(VARCHAR)
    VPSTA = Column(VARCHAR)
    PSTAT = Column(VARCHAR)
    LVORM = Column(VARCHAR)
    MTART = Column(VARCHAR)
    MBRSH = Column(VARCHAR)
    MATKL = Column(VARCHAR)
    BISMT = Column(VARCHAR)
    MEINS = Column(VARCHAR)
    BSTME = Column(VARCHAR)
    ZEINR = Column(VARCHAR)
    ZEIAR = Column(VARCHAR)




class PgMARA(PgBase):
    __tablename__ = 'mara'
    mandt = Column(VARCHAR, primary_key=True)
    matnr = Column(VARCHAR, primary_key=True)
    ersda = Column(VARCHAR)
    ernam = Column(VARCHAR)
    laeda = Column(VARCHAR)
    aenam = Column(VARCHAR)
    vpsta = Column(VARCHAR)
    pstat = Column(VARCHAR)
    lvorm = Column(VARCHAR)
    mtart = Column(VARCHAR)
    mbrsh = Column(VARCHAR)
    matkl = Column(VARCHAR)
    bismt = Column(VARCHAR)
    meins = Column(VARCHAR)
    bstme = Column(VARCHAR)
    zeinr = Column(VARCHAR)
    zeiar = Column(VARCHAR)