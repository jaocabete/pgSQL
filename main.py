import psycopg2
def connect():
    conn = None
    try:
       
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        query = 'select  wo.workorderid from workorder wo '

        cur.execute(query)

        json_data = cur.fetchall()

        if len(json_data) > 0:
            print(str(json_data))
        else:
            print("No data found")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
