from hanadb import SessionHana
from pgdb import  SessionPg

from models import HanaMARA, PgMARA 

from sqlalchemy import select, Insert


with SessionHana() as session:    
    sql = select(HanaMARA.__table__)
    result =session.execute(sql)
    result_list = result.all()
    
## sql query be like : ..brrrr

#text('SELECT "ABAPS417"."MARA"."MANDT", "ABAPS417"."MARA"."MATNR", "ABAPS417"."MARA"."ERSDA", "ABAPS417"."MARA"."ERNAM", "ABAPS417"."MARA"."LAEDA", "ABAPS417"."MARA"."AENAM", "ABAPS417"."MARA"."VPSTA", "ABAPS417"."MARA"."PSTAT", "ABAPS417"."MARA"."LVORM", "ABAPS417"."MARA"."MTART", "ABAPS417"."MARA"."MBRSH", "ABAPS417"."MARA"."MATKL", "ABAPS417"."MARA"."BISMT", "ABAPS417"."MARA"."MEINS", "ABAPS417"."MARA"."BSTME", "ABAPS417"."MARA"."ZEINR", "ABAPS417"."MARA"."ZEIAR" \
#FROM "ABAPS417"."MARA"')
    

with SessionPg() as session:
    for row in result_list:
        stmt = Insert(PgMARA).values(row)
        session.execute(stmt)
        session.commit()

