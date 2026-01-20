import mysql.connector
from psycopg2.extensions import connection
import psycopg2

def connect2dabase() -> connection:
    #docker connection, try/exc
    try:
        connection = psycopg2.connect(
        user="postgres",
        password="password",
        host="localhost",
        port="5432",
        database="meal_planner_db"
        )

    except Exception as error:
        print(f"Error: {error}")

    return connection


def insertrecipe2database(connection, title:str, web_link:str, tags:list[str]) -> None:
    #create the cursor to the database
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print(f"connected to: {record}")
    # insert recipe title and link into recipe data base
    cursor.execute(
        "INSERT INTO recipes (recipe_name, recipe_link) VALUES (%s, %s)",
        (title, web_link)
    )
    recipe_id = cursor.lastrowid

    #loop through all associated tags of recipe adding them to the tables, then make recipe/tag table
    for tag in tags:

        # insert tags if they don't exist, otherwise ignore, error handling
        cursor.execute(
            "INSERT IGNORE INTO tags (tag_name) VALUES (%s)",
            (tag,)
        )

        #get the ID of the tags
        cursor.execute(
            "SELECT id FROM tags WHERE tag_name = %s",
            (tag,)
        )
        tag_id = cursor.fetchone()[0]

        #associate the recipe and tag together
        cursor.execute(
            "INSERT INTO recipe_tags (recipe_id, tag_id) VALUES (%s, %s)",
            (recipe_id, tag_id)
        )

    conn.commit()
2
