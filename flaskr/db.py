import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="john.bielejeski",
                                  password="",
                                  host="localhost",
                                  port="5432",
                                  database="blog")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    insert_query = """ INSERT INTO "post" ("author_id", "title", "body") VALUES (1, 'First post', 'best post')"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from post")
    record = cursor.fetchall()
    print("Result ", record)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

