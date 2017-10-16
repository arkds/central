import psycopg2

from config import DATABASE_URL


def main():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute(open('schema.sql').read())



if __name__ == '__main__':
    main()
