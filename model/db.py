import mysql.connector

def insertdatabase(recipe:str, link:str, tags:list[str]) -> None:
    
    # insert recipe title and link into recipe data base
    cursor.execute(
        "INSERT INTO recipes (recipe_name, recipe_link) VALUES (%s, %s)",
        (name, link)
    )
    recipe_id = cursor.lastrowid

    #loop through all associated tags of recipe adding them to the tables, then join into recipe tags table
    for tag in tags:
        # insert tags if they don't exist, otherwise ignore, error handling
        cursor.execute(
            "INSERT IGNORE INTO tags (tag_name) VALUES (%s)",
            (tag,)
        )
        #get the ID of the tage
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