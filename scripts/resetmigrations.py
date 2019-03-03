import psycopg2
from django.conf import settings

def run(*args):
    db_name = settings.DATABASES['default']['NAME']
    try:
        conn = psycopg2.connect("dbname=%s" % db_name)
        cur = conn.cursor()
        query = "select tablename from pg_catalog.pg_tables where tablename like '{app}_%';".format(app=args[0])
        cur.execute(query)
        for row in cur.fetchall():
            cur.execute("drop table %s cascade;" % row[0])
        cur.execute("delete from django_migrations where app = '%s';" % args[0])
        conn.commit()
    except psycopg2.OperationalError:
        pass